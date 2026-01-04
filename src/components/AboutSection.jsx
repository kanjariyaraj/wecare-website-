import React from 'react';

const AboutSection = () => {
  return (
    <section id="about" className="py-24 overflow-hidden relative bg-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col lg:flex-row items-center gap-16 lg:gap-24">
          {/* Text Content */}
          <div className="lg:w-1/2" data-aos="fade-right">
            <div className="inline-flex items-center px-4 py-2 bg-teal-50 text-teal-700 rounded-full text-xs font-bold mb-8 tracking-widest uppercase border border-teal-100/50">
              Standards & Compliance
            </div>
            <h2 className="text-reveal text-4xl md:text-5xl font-black text-slate-900 leading-[1.15] mb-8 tracking-tight">
              Committed to <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-500 to-blue-600">Secure</span> Healthcare Interoperability.
            </h2>
            <p className="text-lg text-slate-500 leading-relaxed mb-10 font-medium">
              WeCare Lives is aligned with India's National Digital Health Mission. We bridge the gap between clinical excellence and secure digital standards, ensuring that every citizen has access to unified healthcare data at their fingertips.
            </p>

            <div className="space-y-6 mb-12">
              <div className="flex items-start gap-5 p-5 rounded-3xl hover:bg-slate-50 transition-colors duration-300 group" data-aos="fade-up" data-aos-delay="200">
                <div className="w-14 h-14 bg-white shadow-sm border border-slate-100 rounded-2xl flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform duration-500">
                  <svg className="w-7 h-7 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-xl font-bold text-slate-900 mb-1">Uncompromising Trust</h4>
                  <p className="text-slate-500 leading-snug">State-of-the-art encryption protocols ensuring your most sensitive health data remains yours alone.</p>
                </div>
              </div>
              <div className="flex items-start gap-5 p-5 rounded-3xl hover:bg-slate-50 transition-colors duration-300 group" data-aos="fade-up" data-aos-delay="300">
                <div className="w-14 h-14 bg-white shadow-sm border border-slate-100 rounded-2xl flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform duration-500">
                  <svg className="w-7 h-7 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-xl font-bold text-slate-900 mb-1">Universal Accessibility</h4>
                  <p className="text-slate-500 leading-snug">From metropolitan hubs to remote reaches, we connect patients to specialized care instantly.</p>
                </div>
              </div>
              <div className="flex items-start gap-5 p-5 rounded-3xl hover:bg-slate-50 transition-colors duration-300 group" data-aos="fade-up" data-aos-delay="400">
                <div className="w-14 h-14 bg-white shadow-sm border border-slate-100 rounded-2xl flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform duration-500">
                  <svg className="w-7 h-7 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-xl font-bold text-slate-900 mb-1">24/7 Support</h4>
                  <p className="text-slate-500 leading-snug">Our dedicated support team is available around the clock to assist you with any questions or concerns.</p>
                </div>
              </div>
              <div className="flex items-start gap-5 p-5 rounded-3xl hover:bg-slate-50 transition-colors duration-300 group" data-aos="fade-up" data-aos-delay="500">
                <div className="w-14 h-14 bg-white shadow-sm border border-slate-100 rounded-2xl flex items-center justify-center flex-shrink-0 group-hover:scale-110 transition-transform duration-500">
                  <svg className="w-7 h-7 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                </div>
                <div>
                  <h4 className="text-xl font-bold text-slate-900 mb-1">Personalized Experience</h4>
                  <p className="text-slate-500 leading-snug">We tailor your healthcare journey to your specific needs, ensuring a personalized and effective experience.</p>
                </div>
              </div>
            </div>

            {/* Stats Strip */}
            <div className="grid grid-cols-3 gap-8 pt-10 border-t border-slate-100" data-aos="fade-up" data-aos-delay="400">
              <div>
                <div className="text-3xl font-black text-slate-900 tracking-tighter">10k+</div>
                <div className="text-xs text-slate-400 font-bold uppercase tracking-widest mt-1">Global Users</div>
              </div>
              <div>
                <div className="text-3xl font-black text-slate-900 tracking-tighter">500+</div>
                <div className="text-xs text-slate-400 font-bold uppercase tracking-widest mt-1">Verified Clinics</div>
              </div>
              <div>
                <div className="text-3xl font-black text-slate-900 tracking-tighter">99%</div>
                <div className="text-xs text-slate-400 font-bold uppercase tracking-widest mt-1">Uptime</div>
              </div>
            </div>
          </div>

          {/* Visual Side */}
          <div className="lg:w-1/2 relative" data-aos="fade-left">
            <div className="relative z-10 w-full max-w-xl mx-auto rounded-[3.5rem] overflow-hidden shadow-[0_50px_100px_-20px_rgba(0,0,0,0.15)] transform hover:rotate-0 transition-all duration-700 ease-out group cursor-zoom-in">
              <img src="1.jpg" alt="Future of Healthcare" className="w-full h-auto aspect-[4/5] object-cover scale-105 group-hover:scale-100 transition-transform duration-1000 group-hover:brightness-110" />
              <div className="absolute inset-0 bg-gradient-to-tr from-blue-600/20 to-transparent mix-blend-overlay"></div>

              {/* Hover Overlay with Zoom Icon */}
              <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-slate-900/10">
                <div className="bg-white/90 backdrop-blur-md p-4 rounded-full shadow-2xl transform translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                  <svg className="w-8 h-8 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" />
                  </svg>
                </div>
              </div>
            </div>

            {/* Floating Achievement */}
            <div className="absolute -bottom-10 -left-10 z-20 glass p-8 rounded-[2.5rem] shadow-2xl max-w-[240px] border border-white/50 wobble" data-aos="zoom-in" data-aos-delay="600">
              <div className="flex items-center gap-4 mb-4">
                <div className="w-12 h-12 rounded-full bg-teal-500 flex items-center justify-center text-white font-bold italic text-xl shadow-lg shadow-teal-200">W</div>
                <div>
                  <p className="text-[10px] font-black uppercase text-slate-400 tracking-widest leading-none mb-1">Verified Platform</p>
                  <p className="text-sm font-black text-slate-900 leading-none">WeCareLives Trusted</p>
                </div>
              </div>
              <div className="flex -space-x-3">
                <img src="https://i.pravatar.cc/150?u=1" className="w-8 h-8 rounded-full border-2 border-white" alt="User" />
                <img src="https://i.pravatar.cc/150?u=2" className="w-8 h-8 rounded-full border-2 border-white" alt="User" />
                <img src="https://i.pravatar.cc/150?u=3" className="w-8 h-8 rounded-full border-2 border-white" alt="User" />
                <div className="w-8 h-8 rounded-full border-2 border-white bg-slate-100 flex items-center justify-center text-[10px] font-bold text-slate-600">+12k</div>
              </div>
            </div>

            {/* Abstract Decorations */}
            <div className="absolute -top-12 -right-12 w-64 h-64 bg-teal-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse"></div>
            <div className="absolute -bottom-24 -left-24 w-80 h-80 bg-blue-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse" style={{ animationDelay: '2s' }}></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;