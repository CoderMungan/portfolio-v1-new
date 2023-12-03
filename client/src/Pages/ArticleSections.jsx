import { useEffect, useState } from "react"
import { Link } from "react-router-dom"


export default function ArticleSections() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    const apiRequest = async () => {
      const request = await fetch("http://127.0.0.1:8000/article")
      const response = await request.json()
      setPosts(response)
      console.log("gelen api:", response);
    }
    apiRequest()
  }, [])

  return (
    <div className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:mx-0">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">From the Article</h2>
          <p className="mt-2 text-lg leading-8 text-gray-600">
            Some Slogan's here ^^
          </p>
        </div>
        <div className="mx-auto mt-10 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 border-t border-gray-200 pt-10 sm:mt-16 sm:pt-16 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          {posts.map((post) => (
            <article key={post.id} className="flex max-w-xl flex-col items-start justify-between">
              <div className="flex items-center gap-x-4 text-xs">
                <time dateTime={post.createAt} className="text-gray-500">
                  {post.createAt}
                </time>
                  {post.category.title}
              </div>
              <div className="group relative">
                <h3 className="mt-3 text-lg font-semibold leading-6 text-gray-900 group-hover:text-gray-600">
                  <Link to={post.slug}>
                    <span className="absolute inset-0" />
                    {post.title}
                  </Link>
                </h3>
                <p className="mt-5 line-clamp-3 text-sm leading-6 text-gray-600">{post.content}</p>
              </div>
              <div className="relative mt-8 flex items-center gap-x-4">
                <img src={post.image} alt="" className="h-10 w-10 rounded-full bg-gray-50" />
              </div>
            </article>
          ))}
        </div>
      </div>
    </div>
  )
}