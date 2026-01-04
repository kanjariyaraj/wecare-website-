import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-[#0f172a] text-slate-400 pt-24 pb-12 relative overflow-hidden">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-16 mb-20">
          {/* Brand */}
          <div className="lg:col-span-2">
            <a href="#" className="inline-block mb-8">
              <h3 className="text-3xl font-black text-white tracking-tighter">
                WeCare<span className="text-teal-400">Lives</span>
              </h3>
            </a>
            <p className="text-lg leading-relaxed max-w-sm mb-10">
              Pioneering digital healthcare standards in India with secure ABHA integration and patient-first innovation.
            </p>
            <div className="flex gap-4">
              <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex flex-col items-center justify-center text-[10px] font-bold text-teal-400">
                NDHM
              </div>
              <div className="w-12 h-12 rounded-xl bg-white/5 border border-white/10 flex flex-col items-center justify-center text-[10px] font-bold text-teal-400">
                ABDM
              </div>
            </div>
          </div>

          {/* Fast Links */}
          <div>
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-8">Platform</h4>
            <ul className="space-y-4">
              <li><a href="#about" className="hover:text-teal-400 transition-colors flex items-center gap-2 group"><span className="w-1.5 h-1.5 rounded-full bg-teal-500 opacity-0 group-hover:opacity-100 transition-all"></span> About Us</a></li>
              <li><a href="#services" className="hover:text-teal-400 transition-colors flex items-center gap-2 group"><span className="w-1.5 h-1.5 rounded-full bg-teal-500 opacity-0 group-hover:opacity-100 transition-all"></span> Our Services</a></li>
              <li><a href="#solutions" className="hover:text-teal-400 transition-colors flex items-center gap-2 group"><span className="w-1.5 h-1.5 rounded-full bg-teal-500 opacity-0 group-hover:opacity-100 transition-all"></span> Process</a></li>
            </ul>
          </div>

          {/* Support */}
          <div>
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-8">Compliance</h4>
            <ul className="space-y-4">
              <li><a href="#" className="hover:text-teal-400 transition-colors">Privacy Standards</a></li>
              <li><a href="#" className="hover:text-teal-400 transition-colors">Data Security</a></li>
              <li><a href="#" className="hover:text-teal-400 transition-colors">ISO 27001</a></li>
            </ul>
          </div>

          {/* Apps */}
          <div className="lg:w-full">
            <h4 className="text-white font-black uppercase tracking-widest text-sm mb-8">Get the App</h4>
            <div className="flex flex-col gap-4">
              <a href="#" className="group flex items-center gap-4 bg-white/5 border border-white/10 p-4 rounded-2xl hover:bg-white hover:text-slate-900 transition-all duration-500">
                <div className="w-10 h-10 flex items-center justify-center">
                  <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 384 512">
                    <path d="M318.7 268.7c-.2-36.7 16.4-64.4 50-84.8-18.8-26.9-47.2-41.7-84.7-44.6-35.5-2.8-74.3 20.7-88.5 20.7-15 0-49.4-19.7-76.4-19.7C63.3 141.2 4 184.8 4 273.5q0 39.3 14.4 81.2c12.8 36.7 59 126.7 107.2 125.2 25.2-.6 43-17.9 75.8-17.9 31.8 0 48.3 17.9 76.4 17.9 48.6-.7 90.4-82.5 102.6-119.3-39-19.9-59.5-20.2-59.7-59.9zM281.8 100.2c15-18.3 24.4-43 21.4-69.2-22.9 1.3-46 15.4-61.1 33.7-12.8 15.1-23.7 40.8-20.7 65.6 25.2 0 46.6-13.3 60.4-30.1z" />
                  </svg>
                </div>
                <div>
                  <p className="text-[10px] font-black uppercase tracking-widest leading-none mb-1 opacity-50">Download on</p>
                  <p className="text-sm font-bold leading-none">App Store</p>
                </div>
              </a>
              <a href="#" className="group flex items-center gap-4 bg-white/5 border border-white/10 p-4 rounded-2xl hover:bg-white hover:text-slate-900 transition-all duration-500">
                <div className="w-10 h-10 flex items-center justify-center">
                  <svg className="w-8 h-8" fill="currentColor" viewBox="0 0 512 512">
                    <path d="M325.3 234.3L104.6 13l280.8 161.2-60.1 60.1zM47 0C34 6.8 25.3 19.2 25.3 35.3v441.3c0 16.1 8.7 28.5 21.7 35.3l256.6-256L47 0zm425.2 225.6l-58.9-34.1-65.7 64.5 65.7 64.5 60.1-34.1c18-14.3 18-46.5-1.2-60.8zM104.6 499l280.8-161.2-60.1-60.1L104.6 499z" />
                  </svg>
                </div>
                <div>
                  <p className="text-[10px] font-black uppercase tracking-widest leading-none mb-1 opacity-50">Get it on</p>
                  <p className="text-sm font-bold leading-none">Google Play</p>
                </div>
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-12 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
          <p className="text-sm font-medium tracking-wide">
            &copy; 2025 <span className="text-white">WeCareLives Health</span>. All rights reserved.
          </p>
          <div className="flex items-center gap-8 text-xs font-black uppercase tracking-widest">
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-teal-500"></span>
              Status: Operational
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2 h-2 rounded-full bg-blue-500"></span>
              V 2.0.4
            </div>
          </div>
        </div>
      </div>

      {/* Background Accent */}
      <div className="absolute top-0 right-0 w-96 h-96 bg-teal-500/5 rounded-full blur-[120px] -mr-48 -mt-48"></div>
      <div className="absolute bottom-0 left-0 w-96 h-96 bg-blue-500/5 rounded-full blur-[120px] -ml-48 -mb-48"></div>
    </footer>
  );
};

export default Footer;