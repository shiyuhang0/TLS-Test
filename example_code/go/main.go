package main

import (
	"crypto/tls"
	"database/sql"
	"fmt"
	"github.com/go-sql-driver/mysql"
	"log"
)

func main() {

	mysql.RegisterTLSConfig("tidb", &tls.Config{
		MinVersion: tls.VersionTLS12,
		ServerName: "gateway01.us-west-2.prod.aws.tidbcloud.com",
	})

	db, err := sql.Open("mysql", "2a2A3dh5kRV5oPo.root:<your_password>@tcp(gateway01.us-west-2.prod.aws.tidbcloud.com:4000)/test?tls=tidb")
	if err != nil {
		log.Fatal("failed to connect database", err)
	}
	defer db.Close()

	var dbName string
	err = db.QueryRow("SELECT DATABASE();").Scan(&dbName)
	if err != nil {
		log.Fatal("failed to execute query", err)
	}
	fmt.Println(dbName)
}
