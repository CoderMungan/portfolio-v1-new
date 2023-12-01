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
        }
        apiRequest()
    }, [])

    return (
        <>
            <div className="px-4 lg:px-0 mt-12 text-gray-700 max-w-screen-md mx-auto text-lg leading-relaxed">
                {data && (
                    <div key={data.id} className="px-4 lg:px-0 mt-12 text-gray-700 max-w-screen-md mx-auto text-lg leading-relaxed">
                        <h1 className="text-center font-bold text-5xl mb-5">{data.title}</h1>
                        <div className="flex justify-between">
                            <p className="text-center text-sm mb-5">{data.createAt}</p>
                            <p className="text-center text-sm mb-5">{data.category}</p>
                        </div>
                        <p className="pb-6">{data.content}</p>
                    </div>
                )}
            </div>
        </>
    )
}
