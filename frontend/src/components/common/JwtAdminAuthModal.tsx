import React, { useState, useEffect } from 'react';
import { useCMS } from '../../context/CMSContext';
import { ShieldCheck, Lock, Key, Terminal, X, CheckCircle2, AlertCircle, ArrowRight } from 'lucide-react';

export const JwtAdminAuthModal: React.FC = () => {
  const {
    isJwtAuthModalOpen,
    setIsJwtAuthModalOpen,
    loginWithJwt,
    isAdminAuthenticated
  } = useCMS();

  const [email, setEmail] = useState('contactmanojkhatri@gmail.com');
  const [password, setPassword] = useState('admin123');
  const [secretKey, setSecretKey] = useState('django_drf_jwt_secret_key_2026');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [successToken, setSuccessToken] = useState<string | null>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setIsJwtAuthModalOpen(false);
      }
    };
    if (isJwtAuthModalOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isJwtAuthModalOpen, setIsJwtAuthModalOpen]);

  if (!isJwtAuthModalOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      // Simulate JWT Token Authentication Request
      const success = await loginWithJwt(email, password);
      if (success) {
        const dummyToken = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3JfMDAxIiwibmFtZSI6Ik1BTk9KIEsuQy4iLCJyb2xlIjoiU3VwZXIgQWRtaW4iLCJpYXQiOjE3NTQyNDAwMDB9.sig_${Math.random().toString(36).substring(2, 10)}`;
        setSuccessToken(dummyToken);
        setTimeout(() => {
          setLoading(false);
          setIsJwtAuthModalOpen(false);
          setSuccessToken(null);
        }, 1200);
      } else {
        setError('Invalid credentials or JWT token signature. Use email: contactmanojkhatri@gmail.com and password: admin');
        setLoading(false);
      }
    } catch (err) {
      setError('Failed to reach Django REST authentication endpoint.');
      setLoading(false);
    }
  };

  return (
    <div
      onClick={(e) => {
        if (e.target === e.currentTarget) {
          setIsJwtAuthModalOpen(false);
        }
      }}
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in"
    >
      <div className="relative w-full max-w-md bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl p-6 sm:p-8 space-y-6">
        
        {/* Close Button */}
        <button
          type="button"
          aria-label="Close JWT Auth modal"
          onClick={() => setIsJwtAuthModalOpen(false)}
          className="absolute top-4 right-4 p-2 rounded-full text-slate-400 hover:text-white hover:bg-rose-600 transition-all cursor-pointer"
        >
          <X className="w-5 h-5 stroke-[2.5]" />
        </button>

        {/* Modal Header */}
        <div className="space-y-2 text-center">
          <div className="mx-auto w-12 h-12 rounded-2xl bg-indigo-600 text-white flex items-center justify-center shadow-lg shadow-indigo-600/30">
            <Lock className="w-6 h-6" />
          </div>
          <h3 className="text-xl font-black text-slate-900 dark:text-white tracking-tight">
            Django REST JWT Admin Auth
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Secure admin authentication endpoint <code className="font-mono text-indigo-500 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950/60 px-1.5 py-0.5 rounded">POST /api/v1/auth/jwt/token/</code>
          </p>
        </div>

        {/* Error Alert */}
        {error && (
          <div className="p-3.5 rounded-2xl bg-rose-50 dark:bg-rose-950/50 border border-rose-200 dark:border-rose-800 text-rose-700 dark:text-rose-300 text-xs flex items-center gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        {/* Success / Generating Token Animation */}
        {successToken ? (
          <div className="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-200 dark:border-emerald-800 space-y-2 text-center">
            <div className="flex items-center justify-center gap-2 text-emerald-600 dark:text-emerald-400 font-bold text-xs">
              <CheckCircle2 className="w-4 h-4 animate-bounce" /> JWT Auth Verified! Redirecting to CMS...
            </div>
            <p className="font-mono text-[10px] text-emerald-700 dark:text-emerald-300 break-all bg-white dark:bg-slate-950 p-2 rounded-xl border border-emerald-300 dark:border-emerald-900">
              Bearer {successToken.substring(0, 45)}...
            </p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4 text-xs">
            
            <div className="space-y-1.5">
              <label className="font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                <Terminal className="w-3.5 h-3.5 text-indigo-500" /> Admin Email Username
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full px-4 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white font-mono focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="contactmanojkhatri@gmail.com"
              />
            </div>

            <div className="space-y-1.5">
              <label className="font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
                <Key className="w-3.5 h-3.5 text-indigo-500" /> Admin Password
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full px-4 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white font-mono focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="••••••••"
              />
            </div>

            <div className="space-y-1.5">
              <label className="font-bold text-slate-500 dark:text-slate-400 text-[11px] flex items-center gap-1.5">
                <ShieldCheck className="w-3.5 h-3.5 text-slate-400" /> DRF Secret Key (Optional)
              </label>
              <input
                type="text"
                value={secretKey}
                onChange={(e) => setSecretKey(e.target.value)}
                className="w-full px-4 py-2 rounded-xl bg-slate-50 dark:bg-slate-950 border border-slate-200 dark:border-slate-800 text-slate-400 font-mono text-[11px]"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-md shadow-indigo-600/30 transition-all flex items-center justify-center gap-2"
            >
              {loading ? (
                <span>Generating Bearer JWT Token...</span>
              ) : (
                <>
                  <span>Authenticate Admin JWT</span>
                  <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>

            <div className="p-3 rounded-xl bg-slate-100 dark:bg-slate-950 text-[10px] text-slate-500 dark:text-slate-400 font-mono text-center">
              💡 Demo credentials: Email <span className="text-indigo-600 dark:text-indigo-400 font-bold">manojkc1dev@gmail.com</span> / Password <span className="text-indigo-600 dark:text-indigo-400 font-bold">admin123</span>
            </div>

          </form>
        )}

      </div>
    </div>
  );
};
