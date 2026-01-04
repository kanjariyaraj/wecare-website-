import React, { useState } from 'react';

const FAQSection = () => {
  const [activeFAQ, setActiveFAQ] = useState(null);

  const toggleFAQ = (index) => {
    setActiveFAQ(activeFAQ === index ? null : index);
  };

  const faqs = [
    {
      question: 'How do I book an appointment?',
      answer: 'Booking is seamless. Simply download our app, search for verified clinics or specialized doctors near you, select your preferred time slot, and confirm. You\'ll receive instant confirmation and periodic reminders.'
    },
    {
      question: 'Is my health data secure?',
      answer: 'Security is at the heart of Arovita. We employ military-grade AES-256 encryption for all data storage and SSL/TLS protocols for data transmission, ensuring your sensitive medical records are strictly accessible only by you and your authorized providers.'
    },
    {
      question: 'Can I get prescription refills through the app?',
      answer: 'Yes, all your prescriptions are digitized and stored securely. You can easily request refills from your prescribing doctor, and once approved, you can share the digital prescription with pharmacy partners directly through the app.'
    },
    {
      question: 'What emergency services are available?',
      answer: 'Critical situations demand rapid response. Arovita includes a \'SOS\' feature that instantly locates the nearest ER, provides navigation, and can automatically notify your emergency contacts with your current health profile and location.'
    }
  ];

  return (
    <section id="faq" className="py-24 bg-white relative">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-3 gap-16">
          <div className="lg:sticky lg:top-32 h-fit">
            <div className="inline-flex items-center px-4 py-2 bg-blue-50 text-blue-700 rounded-full text-xs font-bold mb-6 tracking-widest uppercase border border-blue-100/50">
              Knowledge Hub
            </div>
            <h2 data-aos="fade-up" className="text-4xl font-black text-slate-900 leading-tight">Frequently<br /><span className="text-blue-600">Asked Questions</span></h2>
            <p data-aos="fade-up" data-aos-delay="100" className="mt-6 text-slate-500 font-medium">
              Everything you need to know about Arovita Health. Can't find the answer? Feel free to contact our support team.
            </p>
            <a href="#contact" className="inline-flex items-center mt-10 text-teal-600 font-black hover:gap-3 transition-all">
              Still have questions? <svg className="ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
            </a>
          </div>

          <div className="lg:col-span-2 space-y-4" data-aos="fade-left">
            {faqs.map((faq, index) => (
              <div key={index} className={`faq-item group bg-slate-50 border border-slate-100 rounded-3xl transition-all duration-300 hover:bg-white hover:shadow-xl hover:shadow-slate-200/50 ${activeFAQ === index ? 'active' : ''}`}>
                <button className="faq-question w-full flex justify-between items-center text-left p-8" onClick={() => toggleFAQ(index)}>
                  <span className="text-xl font-bold text-slate-800 pr-4 group-hover:text-teal-600 transition-colors">{faq.question}</span>
                  <div className="faq-icon-wrapper w-10 h-10 rounded-full bg-white flex items-center justify-center shadow-sm border border-slate-100 group-hover:bg-teal-500 group-hover:text-white transition-all duration-300">
                    <svg className="faq-icon w-5 h-5 transition-transform duration-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="3" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
                    </svg>
                  </div>
                </button>
                <div className="faq-answer max-h-0 overflow-hidden transition-all duration-500 ease-in-out px-8">
                  <p className="pb-8 text-slate-500 font-medium leading-relaxed">
                    {faq.answer}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;