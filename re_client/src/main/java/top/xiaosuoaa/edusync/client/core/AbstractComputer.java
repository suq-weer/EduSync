package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonObject;
import org.apache.logging.log4j.core.util.NetUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.UUID;

public class AbstractComputer {
	private static final Logger LOGGER = LoggerFactory.getLogger(AbstractComputer.class);

	private static String codeBook;
	private static String token;
	private static UUID uuid;

	private static final Network NETWORK;
	private static final ServiceInfo SERVICE_INFO;

	static {
		SERVICE_INFO = new ServiceInfo();
		NETWORK = new Network();
		NETWORK.setResource(Network.Resource.GET_INFO_SOFTWARE_CODEBOOK);
	}

	public AbstractComputer() {
		uuid = UUID.nameUUIDFromBytes(NetUtils.getMacAddress());
	}

	/**
	 * 从网络获取软件密码本
	 * 此方法用于通过网络请求获取软件密码本，解析响应并更新密码本变量
	 * 如果响应状态码不为1或解析失败，则抛出运行时异常
	 */
	private static void getCodeBook() {
		try {
			// 设置网络资源为获取软件密码本信息
			NETWORK.setResource(Network.Resource.GET_INFO_SOFTWARE_CODEBOOK);
			// 发起网络请求并获取响应
			JsonObject response = Network.get(null);
			// 检查响应是否非空且状态码为1
			if (response != null && response.get("error").getAsInt() == 0) {
				// 解析并更新密码本变量
				String rawCodeBook = response.get("data").getAsString();
				// 解码Base64字符串为字节数组
				byte[] decodedBytes = Base64.getDecoder().decode(rawCodeBook);
				// 将字节数组转换为字符串
				codeBook = new String(decodedBytes);
			} else {
				// 如果状态码不是1或无法解析回复内容，抛出异常
				throw new RuntimeException("获取密码本失败（状态码不为1或无法解析回复内容）");
			}
		} catch (Exception e) {
			// 捕获异常并抛出运行时异常，指示获取密码本失败
			throw new RuntimeException("获取密码本失败：", e);
		}
	}

	/**
	 * 获取token方法
	 * 本方法尝试从网络服务中获取token，首先检查近期申请过的token，若不存在或状态不满足条件，则申请新的token
	 * 若获取成功，将token保存在类变量中供后续使用
	 *
	 * @throws RuntimeException 如果获取token失败或状态码不为1，则抛出运行时异常
	 */
	private static void getToken() {
		try {
			//检查近期申请过的token
			NETWORK.setResource(Network.Resource.READ_TOKEN);
			// 构造请求参数，包含设备ID
			String data_o = "type=device_id&data=" + uuid;
			// 发起网络请求获取响应数据
			JsonObject response_o = Network.get(data_o);
			// 检查响应是否不为空且状态码为1，表示请求成功
			if (response_o != null && response_o.get("error").getAsInt() == 0) {
				// 从响应数据中提取token值
				token = response_o.get("data").getAsString();
				// 请求成功并获取到token后，结束当前方法执行
				return;
			}

			//申请新的token
			// 设置网络请求的资源类型为GET_TOKEN
			NETWORK.setResource(Network.Resource.GET_TOKEN);
			// 构造请求参数，包括密码本和设备ID
			String data = "bookCode=" + codeBook + "&device_id=" + uuid;
			// 发起网络请求并获取响应数据
			JsonObject response = Network.get(data);
			// 检查响应是否不为空且状态码为1，表示请求成功
			if (response != null && response.get("error").getAsInt() == 0) {
				// 从响应数据中提取token值
				token = response.get("data").getAsString();
			} else {
				// 如果状态码不是1或无法解析回复内容，则设置token为null并抛出异常
				token = null;
				throw new RuntimeException("状态码不为1或无法解析回复内容");
			}
		} catch (Exception e) {
			token = null;
			throw new RuntimeException("获取token失败：", e);
		}
	}

	public void sync() {
		getCodeBook();
		getToken();
		LOGGER.info("Token sync.");
	}

	void uploadStatus() {
		try {
			this.sync();
			// 设置网络请求的资源类型为UPLOAD_STATUS
			NETWORK.setResource(Network.Resource.UPLOAD_STATUS);
			// 构造请求参数，包括token、设备ID和系统信息
			String tokenEncoded = URLEncoder.encode(token, StandardCharsets.UTF_8);
			String uuidEncoded = URLEncoder.encode(String.valueOf(uuid), StandardCharsets.UTF_8);
			String serviceInfoEncoded = URLEncoder.encode(SERVICE_INFO.getJSONInfo().toString(), StandardCharsets.UTF_8);
			String data = "token=" + tokenEncoded + "&deviceId=" + uuidEncoded + "&data=" + serviceInfoEncoded;
			LOGGER.debug(URLDecoder.decode(serviceInfoEncoded, StandardCharsets.UTF_8));
			JsonObject response = Network.get(data);
			if (response != null && response.get("error").getAsInt() != 0) {
				// 如果状态码为1，表示上传成功
				// 如果状态码不是1或无法解析回复内容，则抛出异常
				throw new RuntimeException("状态码不为1或无法解析回复内容");
			}
			LOGGER.info("Status uploaded.");
		} catch (Exception e) {
			throw new RuntimeException("上传出错：", e);
		}
	}

	public UUID getUUID() {
		return uuid;
	}
}
