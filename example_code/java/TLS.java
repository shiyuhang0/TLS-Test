import java.sql.*;

public class TLS {
  public static void main(String args[]) throws Exception {
    if(args.length !=3) {
      throw new Error("Usage: java TLS_JAVA <host> <port> <database>");
    }
    String user = args[0];
    String host = args[1];
    String password = args[2];
    Class.forName("com.mysql.cj.jdbc.Driver");
    try {
      java.sql.Connection conn = DriverManager.getConnection(
          "jdbc:mysql://" + host + ":4000/test?user=" + user + "&password=" + password + "&sslMode=VERIFY_IDENTITY&enabledTLSProtocols=TLSv1.2,TLSv1.3"
      );
      Statement stmt = conn.createStatement();
      try {
        ResultSet rs = stmt.executeQuery("SELECT DATABASE();");
        if (rs.next()) {
          System.out.println("using db: " + rs.getString(1));
        }
      } catch (Exception e) {
          throw e;
      }
    } catch (Exception e) {
        throw e;
    }
  }
}