<template>
  <mdui-card class="card">
    <mdui-text-field clearable label="搜索..." placeholder="搜索设备名" :value="search_value"
                     @input="search_value = $event.target.value"></mdui-text-field>
    <mdui-button-icon icon="search" @click="searchItem('device_id',search_value)"></mdui-button-icon>
    <div class="actions">
<!--      <mdui-chip icon="add">新增</mdui-chip>-->
<!--      <mdui-chip icon="check">启用</mdui-chip>-->
<!--      <mdui-chip icon="block">禁用</mdui-chip>-->
<!--      <mdui-chip icon="close">删除</mdui-chip>-->
    </div>
    <mdui-list>
      <OnceDeviceListElement
        v-for="item in device_list"
        :key="item.device_id"
        :OnceDeviceListElement_id="item.device_id"
        :OnceDeviceListElement_time="formatTimestamp(item.time * 1000)"
        :OnceDeviceListElement_avatar="getDeviceSystemAvatar(item.data)"
      />
    </mdui-list>
    <div class="count">
      <mdui-chip icon="first_page" @click="handlePageClick('1')" :disabled="currentPage <= 3"></mdui-chip>
      <mdui-chip icon="arrow_back" @click="backPage" :disabled="currentPage <= 1">上一页</mdui-chip>
      <mdui-chip v-for="page in displayedPages" :key="page" @click="handlePageClick(page)">
        <mdui-icon slot="icon" name="location_on" v-if="page === currentPage.toString()"></mdui-icon>
        {{ page }}
      </mdui-chip>
      <mdui-chip icon="arrow_forward" @click="nextPage" :disabled="currentPage >= totalPages">下一页</mdui-chip>
      <mdui-chip icon="last_page" @click="handlePageClick(totalPages.toString())" :disabled="currentPage >= totalPages"></mdui-chip>
    </div>
  </mdui-card>
</template>

<script lang="ts">
import { get_list_device } from '@/api/server'
import { cookie_read_user } from '@/api/manage'
import OnceDeviceListElement from '@/components/OnceDeviceListElement.vue'
import { ref, onMounted, computed } from 'vue'
import { PageController } from '@/api/pages'

export default {
  components: {
    OnceDeviceListElement
  },
  setup() {
    const device_list = ref<{ device_id: string; time: number; data: string }[]>([])
    const currentPage = ref(1)
    const list_length = 10
    const totalPages = ref(1)
    const page_controller = ref<PageController | null>(null)
    const search_value = ref<string>("")

    const fetchDeviceList = async (page: number, length: number, data: string="",value: string="") => {
      try {
        const key = cookie_read_user()['key']
        const uid = cookie_read_user()['uid']

        const result = await get_list_device(uid, key, (page-1).toString(), length.toString(),data,value)
        if (result['status'] !== 0) {
          device_list.value = result['data']
          const totalItems = result['total_list'] || 0
          totalPages.value = Math.ceil(totalItems / length)
          page_controller.value = new PageController(page, totalPages.value)
        } else {
          device_list.value = []
          totalPages.value = 1
          page_controller.value = new PageController(1, 1)
        }
      } catch (error) {
        console.error('Error fetching device list:', error)
      }
    }

    const nextPage = () => {
      if (currentPage.value < totalPages.value) {
        currentPage.value++
        fetchDeviceList(currentPage.value, list_length)
      }
    }

    const backPage = () => {
      if (currentPage.value > 1) {
        currentPage.value--
        fetchDeviceList(currentPage.value, list_length)
      }
    }

    const gotoPage = (page: number) => {
      currentPage.value = page
      fetchDeviceList(currentPage.value, list_length)
    }

    //TODO: 修复省略号点击逻辑
    const handlePageClick = (page: string) => {
      if (page === currentPage.value.toString()) {
        // // Handle ellipsis click
        // if (currentPage.value > 3) {
        //   gotoPage(currentPage.value - 2)
        // } else {
        //   gotoPage(currentPage.value + 2)
        // }
      } else {
        gotoPage(parseInt(page))
      }
    }

    const formatTimestamp = (timestamp: number) => {
      const date = new Date(timestamp);
      return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')} ${String(date.getHours()).padStart(2, '0')}:${String(date.getMinutes()).padStart(2, '0')}:${String(date.getSeconds()).padStart(2, '0')}`
    }

    const getDeviceSystemAvatar = (data: string) => {
      try {
        const obj_data = JSON.parse(atob(data))
        let system = obj_data['SystemOutput']['system']
        let local = './src/assets/logo/'
        const theme = window.matchMedia('(prefers-color-scheme: light)').matches;

        if (system.indexOf('Windows') !== -1) {
          local += 'Windows-' + (theme ? 'Light.svg' : 'Dark.svg')
        } else if (system.indexOf('Linux') !== -1) {
          local += 'Linux-' + (theme ? 'Light.svg' : 'Dark.svg')
        } else {
          local += '../../logo.svg'
        }
        return local
      } catch (error) {
        console.error('Error parsing device data:', error)
        return './src/assets/logo/../../logo.svg'
      }
    }

    const displayedPages = computed(() => {
      if (!page_controller.value) return []
      const result = page_controller.value.getResult()
      const pages = []
      if (result.button_1 === "visible") pages.push(result.button_1_text)
      if (result.button_2 === "visible") pages.push(result.button_2_text)
      if (result.button_3 === "visible") pages.push(result.button_3_text)
      if (result.button_4 === "visible") pages.push(result.button_4_text)
      if (result.button_5 === "visible") pages.push(result.button_5_text)
      return pages
    })

    const searchItem = (data: string,value: string) => {
      console.log(data,value)
      if (value !== "") {
        fetchDeviceList("1", list_length, data, value)
      }else{
        fetchDeviceList("1", list_length)
      }
    }

    onMounted(() => {
      fetchDeviceList(currentPage.value, list_length)
    })

    return {
      device_list,
      currentPage,
      totalPages,
      search_value,
      displayedPages,
      nextPage,
      backPage,
      handlePageClick,
      formatTimestamp,
      getDeviceSystemAvatar,
      searchItem
    }
  }
}
</script>

<style scoped>
@keyframes start {
  from {
    opacity: 0;
    left: 1000px;
  }
  to {
    opacity: 1;
    left: 0;
  }
}

.card {
  animation: start var(--mdui-motion-duration-long4) var(--mdui-motion-easing-emphasized) 0s 1 normal;
  display: block;
  background: rgba(var(--mdui-color-secondary-container));
  width: 100%;
  padding: 1rem;

  .actions,
  .count {
    margin-top: 1rem;
    display: flex;
    gap: 0.5rem;
  }

  mdui-chip {
    margin-left: 0.25rem;
    margin-right: 0.25rem;
    background: rgba(var(--mdui-color-secondary-container));
  }

  mdui-text-field {
    display: inline-block;
    vertical-align: middle;
    width: calc(90% - 0.5rem);
    margin-right: 0.5rem;
    height: 4rem;
  }

  mdui-button-icon {
    display: inline-block;
    vertical-align: middle;
    width: calc(10% - 0.5rem);
    margin-left: 0.5rem;
    height: 4rem;
  }
}
</style>
