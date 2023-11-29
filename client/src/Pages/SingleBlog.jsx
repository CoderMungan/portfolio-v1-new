import { useEffect, useState } from "react"
import { useParams, Link } from "react-router-dom"


export default function SingleBlog() {
    const { slug } = useParams()
    const [data, setData] = useState([])

    useEffect(() => {
        const apiRequest = async () => {
            const request = await fetch(`http://127.0.0.1:8000/article/${slug}`)
            const response = await request.json()
            setData(response)
            console.log("gelen data", response);
        }
        apiRequest()
    }, [])

    return (
        <>
        
        </>
    )
}
