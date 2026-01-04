import React, { useState } from 'react';

const ServicesSection = () => {
  const [activeTab, setActiveTab] = useState('user');

  const switchTab = (type) => {
    setActiveTab(type);
  };

  return (
    <section id="services" className="py-24 bg-white overflow-hidden">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto">
          <h2 className="text-reveal text-4xl md:text-5xl font-extrabold text-slate-900 tracking-tight">
            Verified <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-600 to-blue-600">Health Services</span>
          </h2>
          <p data-aos="fade-up" data-aos-delay="100" className="mt-6 text-lg text-slate-600 leading-relaxed">
            Our services are fully integrated with ABHA, ensuring your records are securely linked and instantly accessible across verified providers.
          </p>
        </div>

        {/* User / Doctor Toggle Tab */}
        <div data-aos="fade-up" data-aos-delay="200" className="mt-12 flex justify-center">
          <div className="relative bg-slate-100 p-1.5 rounded-2xl flex items-center w-full max-w-[320px] shadow-inner">
            {/* Background Slide Indicator */}
            <div id="tab-indicator" className={`tab-indicator absolute h-[calc(100%-12px)] w-[calc(50%-6px)] bg-white rounded-xl shadow-md left-1.5 transition-all ${activeTab === 'doctor' ? 'left-[calc(50%+6px)]' : ''}`}></div>

            <button onClick={() => switchTab('user')} className={`tab-btn ${activeTab === 'user' ? 'active' : ''} relative z-10 w-1/2 py-2.5 text-sm font-bold transition-colors duration-300`}>
              For Patients
            </button>
            <button onClick={() => switchTab('doctor')} className={`tab-btn ${activeTab === 'doctor' ? 'active' : ''} relative z-10 w-1/2 py-2.5 text-sm font-bold text-slate-500 transition-colors duration-300`}>
              For Doctors
            </button>
          </div>
        </div>

        {/* Features Grid */}
        <div id="features-grid" className={`mt-20 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-${activeTab === 'user' ? '4' : '3'} gap-8`}>
          {activeTab === 'user' ? (
            <>
              {/* Feature Card 1 */}
              <div data-aos="fade-up" data-aos-delay="0" className="feature-card relative group p-8 bg-white rounded-[2.5rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-teal-50 flex items-center justify-center transition-all duration-500 group-hover:bg-teal-100">
                  <svg className="icon-svg w-10 h-10 text-teal-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                    <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-teal-600 transition-colors">Verified Clinics</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Access a nationwide network of clinics verified by the National Health Authority for unified care.</p>
              </div>

              {/* Feature Card 2 */}
              <div data-aos="fade-up" data-aos-delay="100" className="feature-card relative group p-8 bg-white rounded-[2.5rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-blue-50 flex items-center justify-center transition-all duration-500 group-hover:bg-blue-100">
                  <svg className="icon-svg w-10 h-10 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-blue-600 transition-colors">Virtual Care</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Encrypted video consultations with instant digital prescription syncing to your ABHA account.</p>
              </div>

              {/* Feature Card 3 */}
              <div data-aos="fade-up" data-aos-delay="200" className="feature-card relative group p-8 bg-white rounded-[2.5rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-indigo-50 flex items-center justify-center transition-all duration-500 group-hover:bg-indigo-100">
                  <svg className="icon-svg w-10 h-10 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors">Digital Reports</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Receive digital lab reports and prescriptions directly into your linked health account.</p>
              </div>

              {/* Feature Card 4 */}
              <div data-aos="fade-up" data-aos-delay="300" className="feature-card relative group p-8 bg-white rounded-[2.5rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-rose-50 flex items-center justify-center transition-all duration-500 group-hover:bg-rose-100">
                  <svg className="icon-svg w-10 h-10 text-rose-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-rose-600 transition-colors">Swift Response</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Emergency access to your medical history for first responders during critical situations.</p>
              </div>
            </>
          ) : (
            <>
              {/* Doctor Feature Card 1 */}
              <div data-aos="fade-up" data-aos-delay="0" className="feature-card relative group p-10 bg-white rounded-[3rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-emerald-50 flex items-center justify-center transition-all duration-500 group-hover:bg-emerald-100">
                  <svg className="icon-svg w-10 h-10 text-emerald-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0h18M12 14.25h.008v.008H12v-.008Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-emerald-600 transition-colors">Appointment Management</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Streamline your clinic operations with a powerful, intuitive scheduling dashboard designed for efficiency.</p>
              </div>

              {/* Doctor Feature Card 2 */}
              <div data-aos="fade-up" data-aos-delay="100" className="feature-card relative group p-10 bg-white rounded-[3rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-cyan-50 flex items-center justify-center transition-all duration-500 group-hover:bg-cyan-100">
                  <svg className="icon-svg w-10 h-10 text-cyan-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 0 0-3.375-3.375h-1.5A1.125 1.125 0 0 1 13.5 7.125v-1.5a3.375 3.375 0 0 0-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 0 0-9-9Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-cyan-600 transition-colors">Prescriptions</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Issue digital prescriptions instantly, ensuring accuracy and providing a seamless patient experience.</p>
              </div>

              {/* Doctor Feature Card 3 */}
              <div data-aos="fade-up" data-aos-delay="200" className="feature-card relative group p-10 bg-white rounded-[3rem] flex flex-col items-center text-center">
                <div className="icon-container w-20 h-20 rounded-3xl bg-indigo-50 flex items-center justify-center transition-all duration-500 group-hover:bg-indigo-100">
                  <svg className="icon-svg w-10 h-10 text-indigo-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                  </svg>
                </div>
                <h3 className="mt-8 text-2xl font-bold text-slate-900 group-hover:text-indigo-600 transition-colors">Medication Adherence</h3>
                <p className="mt-4 text-slate-600 leading-relaxed">Monitor patient progress and improve health outcomes with real-time adherence tracking and notifications.</p>
              </div>
            </>
          )}
        </div>
      </div>
    </section>
  );
};

export default ServicesSection;