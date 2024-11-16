package top.xiaosuoaa.edusync.client.core;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Network {
	private static final String ip = "http://edusync619.yiyu14.top/server/";
	private static String resource;
	private static final HttpClient client = HttpClient.newHttpClient();
	private static final Gson gson = new Gson();

	public Network(String pResource) {
		resource = pResource;
	}

	public static JsonObject get(String data) {
		HttpRequest request = HttpRequest.newBuilder()
				.GET()
				.header("Content-Type", "application/x-www-form-urlencoded")
				.uri(URI.create(ip + resource + "?" + data))
				.build();
		try {
			JsonObject re = gson.fromJson(client.sendAsync(request, HttpResponse.BodyHandlers.ofString()).get().body(), JsonObject.class);
			if (re.get("states").getAsInt() == 1) {
				JsonObject output = new JsonObject();
				output.addProperty("error", 0);
				output.add("data", re.get("data"));
				return output;
			} else {
				throw new Exception(new Throwable("服务器内部异常："+re.get("msg").getAsString()));
			}
		} catch (Exception e) {
			e.fillInStackTrace();
			return null;
		} catch (Throwable e) {
			throw new RuntimeException(e);
		}
	}


	public static JsonObject post(String data) {
		HttpRequest request = HttpRequest.newBuilder()
				.POST(HttpRequest.BodyPublishers.ofString(data))
				.header("Content-Type", "application/x-www-form-urlencoded")
				.uri(URI.create(ip + resource))
				.build();
		try {
			JsonObject re = gson.fromJson(client.sendAsync(request, HttpResponse.BodyHandlers.ofString()).get().body(), JsonObject.class);
			if (re.get("states").getAsInt() == 1) {
				JsonObject output = new JsonObject();
				output.addProperty("error", 0);
				output.add("data", re.get("data"));
				return output;
			} else {
				throw new Exception("服务器内部异常："+re.get("msg").getAsString());
			}
		} catch (Exception e) {
			e.fillInStackTrace();
			return null;
		} catch (Throwable e) {
			throw new RuntimeException(e);
		}
	}


	public String getIp() {
		return ip;
	}

	public String getResource() {
		return resource;
	}
}
