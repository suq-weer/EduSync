package top.xiaosuoaa.edusync.client.core;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Network {
	private static final Logger LOGGER = LoggerFactory.getLogger(Network.class);
	private static final String ip = "http://edusync619.yiyu14.top/server/";
	private static String resource;

	/**
	 * 设置请求资源
	 *
	 * @param resource uri资源，请使用{@link Resource}下的类成员变量。
	 */
	public void setResource(String resource) {
		Network.resource = resource;
	}

	private static final HttpClient client = HttpClient.newHttpClient();
	private static final Gson gson = new Gson();

	public static class Resource {
		public static final String GET_INFO_SOFTWARE_CODEBOOK = "api/get_info_software_codeBook.php/";
		public static final String GET_TOKEN = "function/user/get_token.php";
        public static final String UPLOAD_STATUS = "function/user/upload_device.php";
		public static final String CHECK_COMMAND = "function/user/get_command.php";
        public static final String UPLOAD_COMMAND = "function/user/upload_command.php";
	}

	/**
	 * 发送GET请求并解析响应为JsonObject
	 * 本函数构造一个GET请求，发送到指定的URL，并期望收到一个JSON格式的响应
	 * 它主要用于与服务器交换数据，执行查询等操作
	 *
	 * @param data 请求中携带的数据，以查询字符串的形式附加到URL
	 * @return 返回一个JsonObject，包含服务器响应中的数据如果服务器返回的状态表示失败，则返回null
	 */
	public JsonObject get(String data) {
		// 构建HTTP GET请求
		HttpRequest request = HttpRequest.newBuilder()
				.GET()
				.header("Content-Type", "application/x-www-form-urlencoded")
				.uri(URI.create(ip + resource + "?" + data))
				.build();
		try {
			// 发送请求并解析响应为JsonObject
			String body = client.sendAsync(request, HttpResponse.BodyHandlers.ofString()).get().body();
			JsonObject re = gson.fromJson(body, JsonObject.class);
			// 检查服务器返回的状态码
			if (re.get("states").getAsInt() == 1) {
				// 如果状态码为1，表示成功，则构造并返回包含数据的JsonObject
				JsonObject output = new JsonObject();
				output.addProperty("error", 0);
				output.add("data", re.get("data"));
				return output;
			} else {
				// 如果状态码不为1，表示请求失败，抛出异常
				LOGGER.error("服务器内部异常：{}", re.get("msg").getAsString());
				return null;
			}
		} catch (Throwable e) {
			// 捕获异常，打印堆栈信息，并返回null
			LOGGER.error("网络异常：", e);
			return null;
		}
	}


	/**
	 * 向指定的URI发送POST请求，并解析响应为JsonObject
	 * 此方法主要用于与服务器进行数据交互，发送POST请求并处理响应
	 *
	 * @param data 要发送的数据，通常为表单格式的字符串
	 * @return 返回一个JsonObject，包含服务器响应的数据如果服务器返回错误状态，则返回null
	 * @throws Exception 当服务器返回的状态不是1时，抛出异常，表示服务器内部有异常
	 */
	public JsonObject post(String data) throws Exception {
		// 构建POST请求
		HttpRequest request = HttpRequest.newBuilder()
				.POST(HttpRequest.BodyPublishers.ofString(data))
				.header("Content-Type", "application/x-www-form-urlencoded")
				.uri(URI.create(ip + resource))
				.build();
		// 发送请求并解析响应为JsonObject
		JsonObject re = gson.fromJson(client.sendAsync(request, HttpResponse.BodyHandlers.ofString()).get().body(), JsonObject.class);
		// 检查服务器响应的状态
		if (re.get("states").getAsInt() == 1) {
			// 如果状态为1，表示成功，构建一个新的JsonObject来封装结果
			JsonObject output = new JsonObject();
			output.addProperty("error", 0);
			output.add("data", re.get("data"));
			return output;
		} else {
			// 如果状态不是1，抛出异常，表示服务器内部有异常
			throw new RuntimeException("服务器内部异常：" + re.get("msg").getAsString());
		}
	}
}
