import { useEffect, useState } from "react"
import { useParams, Link } from "react-router-dom"
import { IoMdArrowRoundBack } from "react-icons/io";


export default function SingleArticle() {
    const { slug } = useParams()
    const [data, setData] = useState([])

    useEffect(() => {
        const apiRequest = async () => {
            const request = await fetch(`https://codermungan.pythonanywhere.com/api/article/${slug}`)
            const response = await request.json()
            setData(response)
        }
        apiRequest()
    }, [])

    return (
        <>
            <Link to="/article">
                <p className="max-w-screen-md mx-auto mt-10 text-2xl">
                    <IoMdArrowRoundBack />
                </p>
            </Link>
            {data && (
                <div key={data.id} className="px-4 lg:px-0 mt-10 max-w-screen-md mx-auto text-lg leading-relaxed">
                    <h1 className="text-center font-bold text-5xl">{data.title}</h1>
                    <div className="flex justify-between text-gray-600 mt-10 mb-5">
                        <p className="text-center text-sm">{data.createAt}</p>
                        <p className="text-center text-sm">{data.category}</p>
                    </div>
                    <div className="max-w-screen-md">
                        <p className="pb-6">{data.content}</p>
                    </div>
                </div>
            )}
        </>
    )
}
