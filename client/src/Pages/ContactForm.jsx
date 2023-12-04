import { useState } from "react";

export default function ContactForm() {
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        message: "",
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();


        try {
            const response = await fetch("http://127.0.0.1/contact", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                console.log("Form gönderildi!");
            } else {
                console.error("Form gönderimi başarısız!");
            }
        } catch (error) {
            console.error("Form gönderimi sırasında bir hata oluştu:", error);
        }
    };

    return (
        <div className="flex min-h-screen items-center justify-start bg-white">
            <div className="mx-auto w-full max-w-lg">
                <h1 className="text-4xl font-medium">Contact Me</h1>
                <p className="mt-3">Email us at codermungan@gmail.com or message us here:</p>
                <form onSubmit={handleSubmit} className="mt-10">
                    <div className="grid gap-6 sm:grid-cols-2">
                        <div className="relative z-0">
                            <input
                                type="text"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                className="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" "
                            />
                            <label className="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600 peer-focus:dark:text-blue-500">
                                Your name
                            </label>
                        </div>

                        <div className="relative z-0">
                            <input
                                type="text"
                                name="email"
                                value={formData.email}
                                onChange={handleChange}
                                className="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" "
                            />
                            <label className="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600 peer-focus:dark:text-blue-500">
                                Your email
                            </label>
                        </div>

                        <div className="relative z-0 col-span-2">
                            <textarea
                                name="message"
                                rows="5"
                                value={formData.message}
                                onChange={handleChange}
                                className="peer block w-full appearance-none border-0 border-b border-gray-500 bg-transparent py-2.5 px-0 text-sm text-gray-900 focus:border-blue-600 focus:outline-none focus:ring-0"
                                placeholder=" "
                            ></textarea>
                            <label className="absolute top-3 -z-10 origin-[0] -translate-y-6 scale-75 transform text-sm text-gray-500 duration-300 peer-placeholder-shown:translate-y-0 peer-placeholder-shown:scale-100 peer-focus:left-0 peer-focus:-translate-y-6 peer-focus:scale-75 peer-focus:text-blue-600 peer-focus:dark:text-blue-500">
                                Your message
                            </label>
                        </div>
                    </div>

                    <button type="submit" className="mt-5 rounded-md bg-black px-10 py-2 text-white">
                        Send Message
                    </button>
                </form>
            </div>
        </div>
    );
}
