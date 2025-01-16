package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func getPing(c *gin.Context){
	answer := "Pong"
	c.IndentedJSON(http.StatusOK, answer)
}


func main(){
	router := gin.Default()
	router.GET("ping/", getPing)

	router.Run(":8080")

}