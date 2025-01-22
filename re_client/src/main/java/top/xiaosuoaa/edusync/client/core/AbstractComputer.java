package top.xiaosuoaa.edusync.client.core;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import org.apache.logging.log4j.core.util.NetUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import top.xiaosuoaa.edusync.client.HomeApplication;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.UUID;

public class AbstractComputer {
	private static final Logger LOGGER = LoggerFactory.getLogger(AbstractComputer.class);

	private static String codeBook;
	private static String token;
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
		getCommand();
		uploadStatus();
		LOGGER.info("Token sync.");
	}

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

	private static void getCommand() {
		try {
			NETWORK.setResource(Network.Resource.CHECK_COMMAND);
			String tokenEncoded = URLEncoder.encode(token, StandardCharsets.UTF_8);
			String uuidEncoded = URLEncoder.encode(String.valueOf(uuid), StandardCharsets.UTF_8);
			String data = "token=" + tokenEncoded + "&deviceId=" + uuidEncoded;
			LOGGER.debug(URLDecoder.decode(data, StandardCharsets.UTF_8));
			JsonObject response = Network.get(data);
			if (response != null && response.get("error").getAsInt() == 0) {
				JsonArray dataA = response.get("data").getAsJsonArray();
				for (JsonElement element : dataA) {
					String command = element.getAsJsonObject().get("data").getAsString();
					LOGGER.info("执行命令：{}", command);
					try {
						AbstractPowershellExecutor.executePowerShellCommand(command);
						LOGGER.info("命令执行完成。");
					} catch (Exception e) {
						HomeApplication.showError("执行命令出错：", e, LOGGER);
					}
				}
			}
		} catch (Exception e) {
			throw new RuntimeException("获取命令出错：", e);
		}
	}

	public BigInteger getUUID() {
		return uuid;
	}

	public static class AbstractPowershellExecutor {
		private AbstractPowershellExecutor() {
			String osName = System.getProperty("os.name").toLowerCase();
			if (osName.contains("linux")) {
				installPowerShellOnLinux();
			} else if (osName.contains("windows")) {
				installPowerShellOnWindows();
			} else {
				LOGGER.error("不支持的系统：{}", osName);
			}
		}

		private static void installPowerShellOnWindows() {
			try {
				ProcessBuilder pb = new ProcessBuilder(
						"msiexec.exe", "/i", "path/to/powershell-7.2.23-win-x64.msi", "/quiet", "ADD_PATH=1"
				);
				Process process = pb.start();
				process.waitFor();
				LOGGER.info("PowerShell 在 Windows 上安装成功。");
			} catch (IOException | InterruptedException e) {
				HomeApplication.showError("安装 PowerShell 时出错:", e, LOGGER);
			}
		}

		private static void installPowerShellOnLinux() {
			try {
				ProcessBuilder pb = new ProcessBuilder("bash", "-c", "command -v yay");
				Process process = pb.start();
				process.waitFor();
				if (process.exitValue() == 0) {
					pb = new ProcessBuilder("yay", "-S", "powershell");
					process = pb.start();
					process.waitFor();
					LOGGER.info("使用 yay 安装 PowerShell。");
				} else {
					installPowerShellUsingSnap();
				}
			} catch (IOException | InterruptedException e) {
				HomeApplication.showError("安装 PowerShell 时出错:", e, LOGGER);
			}
		}

		private static void installPowerShellUsingSnap() {
			try {
				ProcessBuilder pb = new ProcessBuilder("sudo", "snap", "install", "powershell", "--classic");
				Process process = pb.start();
				process.waitFor();
				LOGGER.info("使用 snap 安装 PowerShell。");
			} catch (IOException | InterruptedException e) {
				HomeApplication.showError("安装 PowerShell 时出错:", e, LOGGER);
			}
		}

		public static void executePowerShellCommand(String command) {
			try {
				ProcessBuilder pb = new ProcessBuilder("powershell", "-Command", command);
				Process process = pb.start();
				BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
				String line;
				while ((line = reader.readLine()) != null) {
					LOGGER.info(line);
				}
				int exitCode = process.waitFor();
				if (exitCode == 0) {
					LOGGER.info("PowerShell 命令执行成功。");
				} else {
					LOGGER.error("PowerShell 命令执行失败，退出码: {}", exitCode);
				}
			} catch (IOException | InterruptedException e) {
				HomeApplication.showError("执行 PowerShell 命令时出错:", e, LOGGER);
			}
		}
	}
}
