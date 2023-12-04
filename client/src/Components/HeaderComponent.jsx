import Avatar from '../assets/avatar.jpeg';
import ResumePDF from '../assets/GuncelCV.pdf'; // Özgeçmiye PDF dosyasının yolu

export default function HeaderComponent() {
    return (
        <section className="relative isolate overflow-hidden bg-white px-6 py-24 sm:py-32 lg:px-8">
            <div className="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20" />
            <div className="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center" />
            <div className="mx-auto max-w-2xl lg:max-w-4xl">
                <h1 className='text-center text-xl font-semibold leading-8 text-gray-900 sm:text-2xl sm:leading-10 sm:font-bold'>
                    I'm Mehmet Halil MUNGAN 👋
                </h1>
                <figure className="mt-10">
                    <blockquote className="text-center text-sm font-semibold leading-8 text-gray-900 sm:text-sm sm:leading-9">
                        <p>
                            Hi, I'm a web software developer. I unleash my creativity at the keyboard, dancing between the lines of 🐍 Python and Django. The swift rhythm of Redis in data storage excites me, while Django Rest Framework empowers my projects.

                            In the captivating world of the frontend, I dance with 💻 JavaScript and ⚛️ React, illuminating the stage with 🌐 HTML & CSS. My projects are like works of art where technology meets beauty.

                            Are you ready to join this digital dance? Let's feel the rhythm of the code together!
                        </p>
                    </blockquote>
                    <figcaption className="mt-10">
                        <img
                            className="mx-auto h-10 w-10 rounded-full"
                            src={Avatar}
                            alt=""
                        />
                        <div className="mt-4 flex items-center justify-center space-x-3 text-base">
                            <div className="font-semibold text-gray-900">CoderMungan</div>
                            <svg viewBox="0 0 2 2" width={3} height={3} aria-hidden="true" className="fill-gray-900">
                                <circle cx={1} cy={1} r={1} />
                            </svg>
                            <div className="text-gray-600">Software Engineer</div>
                        </div>
                        <div className="mt-4 flex items-center justify-center space-x-3 text-base">
                            <button className="font-semibol bg-gray-800 text-white rounded-3xl w-24 p-1">
                                <a
                                    href={ResumePDF}
                                    target="_blank" // Yeni pencerede açması için
                                    rel="noopener noreferrer"
                                    className="font-semibol bg-gray-800 text-white rounded-3xl w-24 p-1"
                                >
                                    Resume
                                </a>
                            </button>
                        </div>
                    </figcaption>
                </figure>
            </div>
        </section>
    );
}