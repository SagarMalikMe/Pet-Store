import Link from "next/link"
import Head from "next/head"
import styles from "../styles/Home.module.css"
import React,{ useState,useEffect} from "react"

export default function MyApp(){
  const [data, setdata] = useState({})
  useEffect(() => {
    fetch("http://localhost:5000/data").then(
      res =>res.json()
    ).then(
      data => {
        setdata(data)
        console.log(data)
      }
    )

  },[])
  
    return (

        <div> 
          {data.City}
          <p>
            {data.Name} {data.Date}
            {data.programming}
          </p>


        </div>
    )
}


