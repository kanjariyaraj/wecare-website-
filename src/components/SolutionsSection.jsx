import React from 'react';

const SolutionsSection = () => {
  return (
    <section id="solutions" className="py-24 relative overflow-hidden bg-slate-50/50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="text-center max-w-3xl mx-auto mb-20">
          <h2 data-aos="fade-up" className="text-4xl md:text-5xl font-black text-slate-900 tracking-tight leading-tight">
            Simple Process, <span className="text-teal-600 italic">Trusted Care</span>
          </h2>
          <p data-aos="fade-up" data-aos-delay="100" className="mt-6 text-lg text-slate-500 font-medium">
            Getting started with WeCareLives is as easy as 1-2-3. We've streamlined every step to ensure you get the care you deserve.
          </p>
        </div>

        {/* Timeline Container */}
        <div className="relative mt-24">
          {/* Vertical Line (Desktop Only) */}
          <div className="hidden lg:block absolute left-1/2 top-0 bottom-0 w-px bg-gradient-to-b from-transparent via-slate-200 to-transparent transform -translate-x-1/2"></div>

          {/* Step 1 */}
          <div className="flex flex-col lg:flex-row items-center mb-24 last:mb-0 relative group">
            <div className="lg:w-1/2 lg:pr-16 text-center lg:text-right order-2 lg:order-1 mt-10 lg:mt-0" data-aos="fade-right">
              <h3 className="text-3xl font-black text-slate-900 mb-4">Download & Setup</h3>
              <p className="text-lg text-slate-500 leading-relaxed">
                Begin by downloading the WeCareLives app from your favorite app store. Set up your secure profile in minutes and gain instant access to a world-class network of healthcare professionals.
              </p>
            </div>
            <div className="relative flex items-center justify-center order-1 lg:order-2">
              <div className="w-20 h-20 rounded-full bg-white shadow-xl flex items-center justify-center text-2xl font-black text-teal-600 border-4 border-teal-50 z-20 group-hover:scale-110 transition-transform duration-500">01</div>
              <div className="absolute w-24 h-24 bg-teal-100 rounded-full animate-ping opacity-20"></div>
            </div>
            <div className="lg:w-1/2 lg:pl-16 order-3 mt-10 lg:mt-0" data-aos="fade-up-left" data-aos-delay="200">
              <div className="image-container-medium relative group cursor-zoom-in">
                <img src="2.jpg" alt="App Setup" className="img-full rounded-2xl group-hover:scale-105 transition-transform duration-700" />
                {/* Hover Overlay with Zoom Icon */}
                <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-teal-900/10">
                  <div className="bg-white/90 backdrop-blur-md p-3 rounded-full shadow-xl transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <svg className="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Step 2 */}
          <div className="flex flex-col lg:flex-row items-center mb-24 last:mb-0 relative group">
            <div className="lg:w-1/2 lg:pr-16 order-3 lg:order-1 mt-10 lg:mt-0" data-aos="fade-up-right" data-aos-delay="200">
              <div className="image-container-medium relative group cursor-zoom-in">
                <img src="3.webp" alt="Find & Book" className="img-full rounded-2xl group-hover:scale-105 transition-transform duration-700" />
                {/* Hover Overlay with Zoom Icon */}
                <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-blue-900/10">
                  <div className="bg-white/90 backdrop-blur-md p-3 rounded-full shadow-xl transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
            <div className="relative flex items-center justify-center order-1 lg:order-2">
              <div className="w-20 h-20 rounded-full bg-white shadow-xl flex items-center justify-center text-2xl font-black text-blue-600 border-4 border-blue-50 z-20 group-hover:scale-110 transition-transform duration-500">02</div>
              <div className="absolute w-24 h-24 bg-blue-100 rounded-full animate-ping opacity-20" style={{ animationDelay: '1s' }}></div>
            </div>
            <div className="lg:w-1/2 lg:pl-16 text-center lg:text-left order-2 lg:order-3 mt-10 lg:mt-0" data-aos="fade-left">
              <h3 className="text-3xl font-black text-slate-900 mb-4">Discover & Book</h3>
              <p className="text-lg text-slate-500 leading-relaxed">
                Search for certified clinics and top-rated specialists near you. Whether it's an in-person visit or a video consultation, scheduling your appointment is just a few taps away.
              </p>
            </div>
          </div>

          {/* Step 3 */}
          <div className="flex flex-col lg:flex-row items-center relative group">
            <div className="lg:w-1/2 lg:pr-16 text-center lg:text-right order-2 lg:order-1 mt-10 lg:mt-0" data-aos="fade-right">
              <h3 className="text-3xl font-black text-slate-900 mb-4">Recover & Manage</h3>
              <p className="text-lg text-slate-500 leading-relaxed">
                Attend your session and receive digital prescriptions, lab reports, and follow-up plans directly in the app. Stay on track with automated reminders and continuous health tracking.
              </p>
            </div>
            <div className="relative flex items-center justify-center order-1 lg:order-2">
              <div className="w-20 h-20 rounded-full bg-white shadow-xl flex items-center justify-center text-2xl font-black text-rose-600 border-4 border-rose-50 z-20 group-hover:scale-110 transition-transform duration-500">03</div>
              <div className="absolute w-24 h-24 bg-rose-100 rounded-full animate-ping opacity-20" style={{ animationDelay: '2s' }}></div>
            </div>
            <div className="lg:w-1/2 lg:pl-16 order-3 mt-10 lg:mt-0" data-aos="fade-up-left" data-aos-delay="200">
              <div className="image-container-medium relative group cursor-zoom-in">
                <img src="4.webp" alt="Recover & Manage" className="img-full rounded-2xl group-hover:scale-105 transition-transform duration-700" />
                {/* Hover Overlay with Zoom Icon */}
                <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-rose-900/10">
                  <div className="bg-white/90 backdrop-blur-md p-3 rounded-full shadow-xl transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <svg className="w-6 h-6 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                    </svg>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Side background decor labels */}
      <div className="absolute top-1/4 -left-20 text-[10rem] font-black text-slate-200/20 select-none -rotate-90 pointer-events-none">PROCESS</div>
      <div className="absolute bottom-1/4 -right-20 text-[10rem] font-black text-slate-200/20 select-none rotate-90 pointer-events-none">HEALTH</div>
    </section>
  );
};

export default SolutionsSection;