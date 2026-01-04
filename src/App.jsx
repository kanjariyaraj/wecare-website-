import React, { useEffect } from 'react';
import AOS from 'aos';
import 'aos/dist/aos.css';
import Header from './components/Header';
import Hero from './components/Hero';
import ABHASection from './components/ABHASection';
import AboutSection from './components/AboutSection';
import ServicesSection from './components/ServicesSection';
import SolutionsSection from './components/SolutionsSection';
import FAQSection from './components/FAQSection';
import ContactSection from './components/ContactSection';
import Footer from './components/Footer';

function App() {
  useEffect(() => {
    AOS.init({
      duration: 1000,
      once: true,
      offset: 100,
      easing: 'ease-out-back',
      anchorPlacement: 'top-bottom',
    });

    // Scroll Progress Bar Logic
    const scrollProgress = document.getElementById('scroll-progress');
    const handleScroll = () => {
      const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (window.scrollY / totalScroll) * 100;
      scrollProgress.style.width = `${progress}%`;
    };
    window.addEventListener('scroll', handleScroll);

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          const navHeight = 80;
          const elementPosition = targetElement.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - navHeight;

          window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
          });
        }
      });
    });

    // Parallax effect for floating elements
    const parallaxElements = document.querySelectorAll('.parallax');
    const handleParallax = () => {
      let offset = window.pageYOffset;
      parallaxElements.forEach(element => {
        element.style.transform = `translateY(${offset * 0.1}px)`;
      });
    };
    window.addEventListener('scroll', handleParallax);

    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('scroll', handleParallax);
    };
  }, []);

  return (
    <div className="text-slate-700 bg-mint-50/30">
      <div id="scroll-progress" className="scroll-progress"></div>
      <Header />
      <main>
        <Hero />
        <ABHASection />
        <AboutSection />
        <ServicesSection />
        <SolutionsSection />
        <FAQSection />
        <ContactSection />
      </main>
      <Footer />

      {/* Lightbox Modal */}
      <div id="lightbox" className="fixed inset-0 z-[1000] hidden items-center justify-center bg-slate-900/95 backdrop-blur-xl opacity-0 transition-opacity duration-400">
        <button className="absolute top-8 right-10 text-white hover:scale-110 transition-transform z-[1010]" onClick={() => closeLightbox()}>
          <svg className="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        <img id="lightbox-img" src="" className="max-w-[90%] max-h-[90%] rounded-[2rem] shadow-2xl transform scale-90 transition-transform duration-400" alt="Full Image View" />
      </div>
    </div>
  );
}

// Lightbox functions
function openLightbox(src) {
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  img.src = src;
  lightbox.classList.remove('hidden');
  lightbox.classList.add('flex');
  setTimeout(() => {
    lightbox.classList.add('active');
    lightbox.style.opacity = '1';
    img.style.transform = 'scale(1)';
  }, 10);
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const lightbox = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  lightbox.style.opacity = '0';
  img.style.transform = 'scale(0.9)';
  setTimeout(() => {
    lightbox.classList.remove('active');
    lightbox.classList.remove('flex');
    lightbox.classList.add('hidden');
    document.body.style.overflow = '';
  }, 400);
}

// Close on Escape key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeLightbox();
});

// Make functions global
window.openLightbox = openLightbox;
window.closeLightbox = closeLightbox;

export default App;