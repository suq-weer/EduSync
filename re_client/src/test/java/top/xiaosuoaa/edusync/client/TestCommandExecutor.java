package top.xiaosuoaa.edusync.client;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import top.xiaosuoaa.edusync.client.core.AbstractComputer;

public class TestCommandExecutor {
	public static void main(String[] args) {
		Gson gson = new Gson();
		AbstractComputer computer = new AbstractComputer();
		AbstractComputer.CommandExecutor executor = new AbstractComputer.CommandExecutor(computer, "powershell.exe /c dir", 1);
		JsonObject result = executor.execute();
		System.out.println(gson.fromJson(result, JsonObject.class).get("output").getAsString());
	}
}
