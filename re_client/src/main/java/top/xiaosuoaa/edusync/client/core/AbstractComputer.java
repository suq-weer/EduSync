package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import org.apache.logging.log4j.core.util.NetUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import top.xiaosuoaa.edusync.client.HomeApplication;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.UUID;

public class AbstractComputer {
	private static final Logger LOGGER = LoggerFactory.getLogger(AbstractComputer.class);

	private static String codeBook;
	private static String token;

	public static BigInteger getUuid() {
		return uuid;
	}

	private static BigInteger uuid;

	private static final Network NETWORK;
	private static final ServiceInfo SERVICE_INFO;

	static {
		SERVICE_INFO = new ServiceInfo();
		NETWORK = new Network();
		NETWORK.setResource(Network.Resource.GET_INFO_SOFTWARE_CODEBOOK);
	}

	public AbstractComputer() {
		uuid = new BigInteger(UUID.nameUUIDFromBytes(NetUtils.getMacAddress()).toString().replace("-", ""), 16);
	}

	/**
	 * 从网络获取软件密码本
	 * 此方法用于通过网络请求获取软件密码本，解析响应并更新密码本变量
	 * @throws RuntimeException 如果获取密码本失败或状态码不为1，则抛出运行时异常
	 */
	private static void getCodeBook() {
		try {
			// 设置网络资源为获取软件密码本信息
			NETWORK.setResource(Network.Resource.GET_INFO_SOFTWARE_CODEBOOK);
			// 发起网络请求并获取响应
			JsonObject response = NETWORK.get(null);
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
			JsonObject response_o = NETWORK.get(data_o);
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
			JsonObject response = NETWORK.get(data);
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

	/**
	 * 主同步方法
	 *
	 * @see #getCodeBook()
	 * @see #getToken()
	 * @see #getCommand()
	 * @see #uploadStatus()
	 */
	public void sync() {
		getCodeBook();
		getToken();
		getCommand();
		uploadStatus();
		LOGGER.info("Token sync.");
	}

	/**
	 * 上传状态信息到服务器
	 * 此方法负责将设备的状态信息上传到服务器，包括设备的token、设备ID和系统信息
	 * 它通过网络请求实现上传功能，并根据服务器返回的状态码判断上传是否成功
	 *
	 * @throws RuntimeException 如果上传过程中发生错误或服务器返回错误状态码，则抛出运行时异常
	 */
	private static void uploadStatus() {
		try {
			// 设置网络请求的资源类型为UPLOAD_STATUS
			NETWORK.setResource(Network.Resource.UPLOAD_STATUS);
			// 构造请求参数，包括token、设备ID和系统信息
			String tokenEncoded = URLEncoder.encode(token, StandardCharsets.UTF_8);
			String uuidEncoded = URLEncoder.encode(String.valueOf(uuid), StandardCharsets.UTF_8);
			String serviceInfoEncoded = URLEncoder.encode(SERVICE_INFO.getJSONInfo().toString(), StandardCharsets.UTF_8);
			String data = "token=" + tokenEncoded + "&deviceId=" + uuidEncoded + "&data=" + serviceInfoEncoded;
			LOGGER.debug(URLDecoder.decode(serviceInfoEncoded, StandardCharsets.UTF_8));
			JsonObject response = NETWORK.get(data);
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

	/**
	 * 获取并执行命令的方法
	 * 该方法负责与服务器通信，获取待执行的命令，执行命令，并上传执行结果
	 */
	private void getCommand() {
		try {
			// 设置网络资源为检查命令
			NETWORK.setResource(Network.Resource.CHECK_COMMAND);
			// 对token和uuid进行URL编码，以适应网络传输
			String tokenEncoded = URLEncoder.encode(token, StandardCharsets.UTF_8);
			String uuidEncoded = URLEncoder.encode(String.valueOf(uuid), StandardCharsets.UTF_8);
			// 构造请求数据
			String data = "token=" + tokenEncoded + "&deviceId=" + uuidEncoded;
			// 记录请求数据，便于调试
			LOGGER.debug(URLDecoder.decode(data, StandardCharsets.UTF_8));
			// 发送请求，获取响应
			JsonObject response = NETWORK.get(data);
			// 检查响应是否成功
			if (response != null && response.get("error").getAsInt() == 0) {
				// 解析响应数据，获取命令数组
				JsonArray dataA = response.get("data").getAsJsonArray();
				// 初始化命令执行结果数组
				JsonArray commands = new JsonArray();
				// 遍历命令数组，执行每个命令
				for (JsonElement element : dataA) {
					String command = element.getAsJsonObject().get("data").getAsString();
					int type = element.getAsJsonObject().get("type").getAsInt();
					// 记录命令执行信息
					LOGGER.info("执行命令：{}", command);
					try {
						// 创建命令执行器并执行命令
						CommandExecutor executor = new CommandExecutor(this, command, type);
						commands.add(executor.execute());
						// 设置网络资源为上传命令结果
						NETWORK.setResource(Network.Resource.UPLOAD_COMMAND);
						// 构造上传命令结果的数据
						String commandData = "token=" + tokenEncoded + "&deviceId=" + uuidEncoded + "&commandId=" + element.getAsJsonObject().get("id").getAsString() + "&data=" + commands.getAsString();
						// 发送请求，上传命令执行结果
						JsonObject uploadResponse = NETWORK.post(commandData);
						// 检查上传结果是否成功
						if (uploadResponse.get("error").getAsInt() != 0) {
							HomeApplication.showError("上传命令出错：", new Exception(uploadResponse.get("data").getAsString()), LOGGER);
						}
						// 记录命令执行完成信息
						LOGGER.info("命令执行完成。");
					} catch (Exception e) {
						// 处理命令执行时的异常
						HomeApplication.showError("执行命令出错：", e, LOGGER);
					}
				}
			}
		} catch (Exception e) {
			// 处理获取命令时的异常
			throw new RuntimeException("获取命令出错：", e);
		}
	}

	public BigInteger getUUID() {
		return uuid;
	}

	public static class CommandExecutor {
		private static AbstractComputer computer;
		private static ProcessBuilder processBuilder;
		private static List<String> outputList = new ArrayList<>();
		private static List<String> errorList = new ArrayList<>();
		private static String command;
		private static int type;

		public CommandExecutor(AbstractComputer IComputer, String ICommand, int IType) {
			computer = IComputer;
			command = ICommand;
			type = IType;
			processBuilder = new ProcessBuilder(command);
		}

		/**
		 * 执行预定义命令并返回结果
		 * 此方法启动一个进程来执行命令，并捕获其输出和错误流
		 * 如果计算机对象、命令或类型未正确设置，则返回null
		 *
		 * @return 返回一个包含执行结果的JsonObject，包括退出代码、输出和错误信息；如果执行失败，返回null
		 * @throws RuntimeException 如果执行过程中发生IOException或InterruptedException，则抛出RuntimeException
		 */
		public JsonObject execute() {
			// 检查必要条件是否满足
			if (computer == null || command == null || type == 0) {
				return null;
			}
			try {
				// 启动进程
				Process process = processBuilder.start();
				// 读取并处理进程的输出流
				readStream(process.getInputStream(), "OUTPUT");
				// 读取并处理进程的错误流
				readStream(process.getErrorStream(), "ERROR");
				// 等待进程执行完成并获取退出代码
				int exitCode = process.waitFor();
				// 创建一个JSON对象来存储执行结果
				JsonObject output = new JsonObject();
				// 添加退出代码到结果中
				output.add("result", new JsonPrimitive(exitCode));
				// 添加输出流信息到结果中
				output.add("output", new JsonPrimitive(String.join("\n", outputList)));
				// 添加错误流信息到结果中
				output.add("error", new JsonPrimitive(String.join("\n", errorList)));
				// 返回执行结果
				return output;
			} catch (IOException | InterruptedException e) {
				// 如果发生异常，抛出RuntimeException
				throw new RuntimeException(e);
			}
		}

		/**
		 * 从输入流中读取数据，并根据数据类型存储到相应的列表中
		 * 此方法用于处理不同类型的流，将流中的每一行数据添加到一个列表中，
		 * 并根据是输出流还是错误流，将数据分配到对应的列表变量中
		 *
		 * @param inputStream 输入流，可以是程序的输出流或错误流
		 * @param type        流的类型，用于标识是输出流还是错误流，当前实现中使用"OUTPUT"来标识输出流
		 */
		private static void readStream(InputStream inputStream, String type) {
			try (BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
				List<String> list = new ArrayList<>();
				String line;
				// 循环读取流中的每一行数据，直到流结束
				while ((line = reader.readLine()) != null) {
					list.add(type + ":" + line);
				}
				// 根据流的类型，将读取的数据分配到对应的列表变量中
				if (type.equals("OUTPUT")) {
					outputList = list;
				} else {
					errorList = list;
				}
			} catch (IOException e) {
				// 如果在读取流时发生IO异常，将其转换为运行时异常并抛出
				throw new RuntimeException(e);
			}
		}
	}
}
