import React from 'react';

const ABHASection = () => {
  return (
    <section id="abha" className="py-24 bg-white relative overflow-hidden">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-16">
          {/* Info Panel */}
          <div className="lg:w-1/2" data-aos="fade-right">
            <div className="inline-flex items-center px-4 py-2 bg-teal-50 text-teal-700 rounded-full text-xs font-bold mb-8 tracking-widest uppercase border border-teal-100/50">
              Digital Health Identity
            </div>
            <h2 className="text-reveal text-4xl md:text-5xl font-black text-slate-900 leading-[1.15] mb-8 tracking-tight">
              What is <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-500 to-blue-600">ABHA ID</span>?
            </h2>
            <p className="text-lg text-slate-500 leading-relaxed mb-10 font-medium">
              The Ayushman Bharat Health Account (ABHA) is your unique identity in India's digital healthcare ecosystem. It empowers you to store, share, and access your medical records digitally across any healthcare provider in the nation securely.
            </p>

            {/* Trust Badge */}
            <div className="flex items-center gap-4 p-6 bg-slate-50 rounded-[2rem] border border-slate-100 mb-12">
              <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center shadow-sm flex-shrink-0">
                <svg className="w-10 h-10 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                </svg>
              </div>
              <div>
                <h4 className="text-lg font-bold text-slate-900">Government Approved</h4>
                <p className="text-sm text-slate-500 font-medium">Compliant with National Digital Health Mission standards.</p>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-6">
              <div className="p-6 bg-white border border-slate-100 rounded-3xl hover:shadow-xl transition-all duration-300">
                <div className="w-12 h-12 bg-blue-50 rounded-2xl flex items-center justify-center mb-4">
                  <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
                  </svg>
                </div>
                <h5 className="text-base font-bold text-slate-900 mb-1">Secure Records</h5>
                <p className="text-xs text-slate-500 leading-snug">Encrypted storage for all your health history.</p>
              </div>
              <div className="p-6 bg-white border border-slate-100 rounded-3xl hover:shadow-xl transition-all duration-300">
                <div className="w-12 h-12 bg-teal-50 rounded-2xl flex items-center justify-center mb-4">
                  <svg className="w-6 h-6 text-teal-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
                  </svg>
                </div>
                <h5 className="text-base font-bold text-slate-900 mb-1">Nationwide Access</h5>
                <p className="text-xs text-slate-500 leading-snug">Use your health data anywhere in India.</p>
              </div>
            </div>
          </div>

          {/* Setup Flow Visual */}
          <div className="lg:w-1/2" data-aos="fade-left">
            <div className="bg-slate-900 rounded-[3.5rem] p-10 shadow-2xl relative">
              {/* Glow */}
              <div className="absolute -top-10 -right-10 w-64 h-64 bg-teal-500/20 rounded-full blur-3xl"></div>

              <h3 className="text-2xl font-bold text-white mb-10 text-center">How to Link ABHA ID</h3>

              <div className="space-y-12">
                <div className="flex gap-6 relative">
                  <div className="absolute left-6 top-12 bottom-0 w-0.5 bg-slate-800"></div>
                  <div className="w-12 h-12 bg-teal-600 rounded-full flex items-center justify-center text-white font-black z-10 shrink-0">01</div>
                  <div className="pt-2">
                    <h4 className="text-lg font-bold text-white mb-1">Enter ABHA Number</h4>
                    <p className="text-sm text-slate-400">Use your 14-digit ABHA number or address.</p>
                  </div>
                </div>
                <div className="flex gap-6 relative">
                  <div className="absolute left-6 top-12 bottom-0 w-0.5 bg-slate-800"></div>
                  <div className="w-12 h-12 bg-teal-600 rounded-full flex items-center justify-center text-white font-black z-10 shrink-0">02</div>
                  <div className="pt-2">
                    <h4 className="text-lg font-bold text-white mb-1">Instant Verification</h4>
                    <p className="text-sm text-slate-400">Quick OTP-based secure verification via Mobile.</p>
                  </div>
                </div>
                <div className="flex gap-6">
                  <div className="w-12 h-12 bg-teal-600 rounded-full flex items-center justify-center text-white font-black z-10 shrink-0">03</div>
                  <div className="pt-2">
                    <h4 className="text-lg font-bold text-white mb-1">Unified Health Profile</h4>
                    <p className="text-sm text-slate-400">All your records synced and ready for care.</p>
                  </div>
                </div>
              </div>

              <div className="mt-12 text-center">
                <button className="w-full bg-white text-slate-900 font-bold py-4 rounded-2xl hover:bg-teal-50 transition-colors shadow-xl">
                  Start Linking Now
                </button>
                <p className="mt-4 text-[10px] text-slate-500 uppercase tracking-widest font-black">Powered by National Health Authority</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ABHASection;