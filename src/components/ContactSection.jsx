import React from 'react';

const ContactSection = () => {
  return (
    <section id="contact" className="py-24 relative overflow-hidden">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="max-w-6xl mx-auto bg-white rounded-[3rem] shadow-[0_50px_100px_-20px_rgba(0,0,0,0.1)] overflow-hidden border border-slate-100">
          <div className="flex flex-col lg:flex-row">
            {/* Left: Info Column */}
            <div className="lg:w-2/5 bg-slate-900 p-12 lg:p-16 text-white relative">
              <div className="relative z-10">
                <h2 className="text-4xl font-black mb-6">Secure <span className="text-teal-400">Communication</span></h2>
                <p className="text-slate-400 text-lg mb-12">Connect with our verified support team for any integration or health account inquiries.</p>

                <div className="space-y-8">
                  <div className="flex items-start gap-6 group">
                    <div className="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center text-teal-400 group-hover:bg-teal-500 group-hover:text-white transition-all duration-300">
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <div>
                      <p className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-1">Official Email</p>
                      <a href="mailto:support@WeCareLives.in" className="text-xl font-bold hover:text-teal-400 transition-colors">support@WeCareLives.in</a>
                    </div>
                  </div>
                  <div className="flex items-start gap-6 group">
                    <div className="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center text-blue-400 group-hover:bg-blue-500 group-hover:text-white transition-all duration-300">
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                      </svg>
                    </div>
                    <div>
                      <p className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-1">Call us</p>
                      <p className="text-xl font-bold">+91 9574332484</p>
                    </div>
                  </div>
                  <div className="flex items-start gap-6 group">
                    <div className="w-12 h-12 rounded-2xl bg-white/10 flex items-center justify-center text-purple-400 group-hover:bg-purple-500 group-hover:text-white transition-all duration-300">
                      <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                      </svg>
                    </div>
                    <div>
                      <p className="text-xs font-bold text-slate-500 uppercase tracking-widest mb-1">Office</p>
                      <p className="text-lg font-bold">jamangar ,digvijay plot</p>
                      <p className="text-slate-500">gujrat, 3651005</p>
                    </div>
                  </div>
                </div>
              </div>
              {/* Background Decor */}
              <div className="absolute top-0 right-0 w-64 h-64 bg-teal-500/10 rounded-full -mr-32 -mt-32 blur-3xl"></div>
              <div className="absolute bottom-0 left-0 w-64 h-64 bg-blue-500/10 rounded-full -ml-32 -mb-32 blur-3xl"></div>
            </div>

            {/* Right: Form Column */}
            <div className="lg:w-3/5 p-12 lg:p-16">
              <form action="#" method="POST" className="space-y-6">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  <div>
                    <label htmlFor="name" className="block text-sm font-black text-slate-900 uppercase tracking-widest mb-2">FullName</label>
                    <input type="text" id="name" name="name" placeholder="John Doe" className="w-full px-6 py-4 bg-slate-50 border-0 rounded-2xl focus:ring-2 focus:ring-teal-500 transition-all placeholder:text-slate-400" />
                  </div>
                  <div>
                    <label htmlFor="email" className="block text-sm font-black text-slate-900 uppercase tracking-widest mb-2">Email Address</label>
                    <input type="email" id="email" name="email" placeholder="john@example.com" className="w-full px-6 py-4 bg-slate-50 border-0 rounded-2xl focus:ring-2 focus:ring-teal-500 transition-all placeholder:text-slate-400" />
                  </div>
                </div>
                <div>
                  <label htmlFor="subject" className="block text-sm font-black text-slate-900 uppercase tracking-widest mb-2">Subject</label>
                  <input type="text" id="subject" name="subject" placeholder="Inquiry about..." className="w-full px-6 py-4 bg-slate-50 border-0 rounded-2xl focus:ring-2 focus:ring-teal-500 transition-all placeholder:text-slate-400" />
                </div>
                <div>
                  <label htmlFor="message" className="block text-sm font-black text-slate-900 uppercase tracking-widest mb-2">Your Message</label>
                  <textarea id="message" name="message" rows="5" placeholder="Tell us more about..." className="w-full px-6 py-4 bg-slate-50 border-0 rounded-2xl focus:ring-2 focus:ring-teal-500 transition-all placeholder:text-slate-400 resize-none"></textarea>
                </div>
                <button type="submit" className="w-full bg-teal-600 text-white font-black py-5 px-8 rounded-2xl hover:bg-teal-700 transition-all duration-300 shadow-xl shadow-teal-900/20 group flex items-center justify-center gap-3">
                  Send Message
                  <svg className="w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="3" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
      {/* Background Blob */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full max-w-4xl max-h-4xl bg-gradient-to-tr from-teal-100/20 to-blue-100/20 rounded-full blur-3xl -z-10 animate-pulse"></div>
    </section>
  );
};

export default ContactSection;