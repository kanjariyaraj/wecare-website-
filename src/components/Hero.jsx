import React from 'react';

const Hero = () => {
  return (
    <section id="home" className="relative pt-32 pb-20 lg:pt-56 lg:pb-36 overflow-hidden">
      <div className="hero-glow"></div>
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        <div data-aos="fade-down" className="inline-flex items-center space-x-2 px-3 py-1 bg-teal-50 border border-teal-100 rounded-full text-teal-700 text-xs font-bold uppercase tracking-widest mb-8">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-teal-500"></span>
          </span>
          <span>Government-Approved Digital Healthcare</span>
        </div>

        <h1 data-aos="fade-up" className="text-reveal text-5xl md:text-7xl font-black text-slate-900 leading-[1.1] tracking-tight">
          Your <span className="text-transparent bg-clip-text bg-gradient-to-br from-teal-500 to-teal-600">Health</span>,<br />
          Unified with <span className="text-transparent bg-clip-text bg-gradient-to-br from-blue-500 to-blue-600">ABHA</span>.
        </h1>

        <p data-aos="fade-up" data-aos-delay="150" className="mt-8 max-w-2xl mx-auto text-lg md:text-xl text-slate-500 leading-relaxed font-medium">
          The next era of Indian healthcare is here. Seamlessly link your ABHA ID to access digital records,
          verified clinics, and nationwide care—all in one secure platform.
        </p>

        <div data-aos="fade-up" data-aos-delay="300" className="mt-12 flex flex-col sm:flex-row justify-center items-center gap-6">
          <a href="#abha" className="w-full sm:w-auto bg-teal-600 text-white font-bold px-10 py-4 rounded-2xl text-lg hover:bg-teal-700 transition-all hover:shadow-2xl hover:-translate-y-1 duration-300 hover:shadow-teal-500/40">
            Link Your ABHA ID
          </a>
          <a href="#solutions" className="w-full sm:w-auto bg-white text-slate-900 border border-slate-200 font-bold px-10 py-4 rounded-2xl text-lg hover:bg-slate-50 transition-all hover:shadow-xl hover:-translate-y-1 duration-300">
            How it Works
          </a>
        </div>

        {/* Floating elements decor */}
        <div className="hidden lg:block absolute -left-20 top-1/2 -translate-y-1/2 w-48 h-48 bg-blue-100/30 rounded-full blur-3xl parallax"></div>
        <div className="hidden lg:block absolute -right-20 top-1/2 -translate-y-1/2 w-48 h-48 bg-teal-100/30 rounded-full blur-3xl parallax"></div>
      </div>
    </section>
  );
};

export default Hero;