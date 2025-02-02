export class pageController {
  constructor(current_page:number , max_page_count: number) {
    this.current_page = current_page; // 定义并初始化 name 属性
    this.max_page_count = max_page_count;

    if (this.max_page_count===0||this.max_page_count===1){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = "1"

      //按钮2
      this.button_2 = "none"
      this.button_2_text = "2"

      //按钮3
      this.button_3 = "none"
      this.button_3_text = "3"

      //按钮4
      this.button_4 = "none"
      this.button_4_text = "......"

      //按钮5
      this.button_5 = "none"
      this.button_5_text = "619"
    }
    else if (this.max_page_count===2){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = "1"

      //按钮2
      this.button_2 = "visible"
      this.button_2_text = "2"

      //按钮3
      this.button_3 = "none"
      this.button_3_text = "3"

      //按钮4
      this.button_4 = "none"
      this.button_4_text = "......"

      //按钮5
      this.button_5 = "none"
      this.button_5_text = "619"
    }
    else if (this.max_page_count===3){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = "1"

      //按钮2
      this.button_2 = "visible"
      this.button_2_text = "2"

      //按钮3
      this.button_3 = "visible"
      this.button_3_text = "3"

      //按钮4
      this.button_4 = "none"
      this.button_4_text = "......"

      //按钮5
      this.button_5 = "none"
      this.button_5_text = "619"
    }
    else if (this.max_page_count===4){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = "1"

      //按钮2
      this.button_2 = "visible"
      this.button_2_text = "2"

      //按钮3
      this.button_3 = "visible"
      this.button_3_text = "3"

      //按钮4
      this.button_4 = "none"
      this.button_4_text = "......"

      //按钮5
      this.button_5 = "visible"
      this.button_5_text = "4"
    }
    else if (this.max_page_count===5){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = "1"

      //按钮2
      this.button_2 = "visible"
      this.button_2_text = "2"

      //按钮3
      this.button_3 = "visible"
      this.button_3_text = "3"

      //按钮4
      this.button_4 = "visible"
      this.button_4_text = "4"

      //按钮5
      this.button_5 = "visible"
      this.button_5_text = "5"
    }
    else if (this.max_page_count>5){
      //按钮1
      this.button_1 = "visible"
      this.button_1_text = this.current_page-2

      //按钮2
      this.button_2 = "visible"
      this.button_2_text = this.current_page-1

      //按钮3
      this.button_3 = "visible"
      this.button_3_text = "......"

      //按钮4
      this.button_4 = "visible"
      this.button_4_text = this.current_page+1

      //按钮5
      this.button_5 = "visible"
      this.button_5_text = this.current_page+2
    }

    this.result = {
      "current_page": this.current_page,
      "max_page_count": this.max_page_count,

      "button_1" : this.button_1,
      "button_1_text" : this.button_2_text,

      "button_2" : this.button_2,
      "button_2_text" : this.button_2_text,

      "button_3" : this.button_3,
      "button_3_text" : this.button_3_text,

      "button_4" : this.button_4,
      "button_4_text" : this.button_4_text,

      "button_5" : this.button_5,
      "button_5_text" : this.button5_text,
    }
  }


  nextPage(){
    if (this.current_page<this.max_page_count){
      this.current_page += 1
      // console.log(this.current_page)
    }
    console.log(this.max_page_count)
    return this.result
  }

  backPage(){
    if (this.current_page!==1){
      this.current_page -= 1
    }
    return this.result
  }


}