import React, { useState, useEffect } from 'react';
import toast, { Toaster } from 'react-hot-toast';
import ImageUpload from './components/ImageUpload';
import ResultsDisplay from './components/ResultsDisplay';
import { analyzeTongue, getHealthStatus } from './services/api';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [healthStatus, setHealthStatus] = useState(null);

  useEffect(() => {
    fetchHealthStatus();
  }, []);

  const fetchHealthStatus = async () => {
    try {
      const status = await getHealthStatus();
      setHealthStatus(status);
    } catch (error) {
      console.warn('Health check failed:', error);
    }
  };

  const handleImageSelect = (file) => {
    setSelectedFile(file);
    const reader = new FileReader();
    reader.onload = (e) => {
      setImagePreview(e.target.result);
    };
    reader.readAsDataURL(file);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      toast.error('Please select an image first');
      return;
    }

    setIsLoading(true);
    try {
      toast.loading('Analyzing image...', { id: 'analyzing' });
      const result = await analyzeTongue(selectedFile);
      setAnalysisResult(result);
      toast.dismiss('analyzing');
      toast.success('Analysis complete!');
    } catch (error) {
      toast.dismiss('analyzing');
      toast.error('Failed to analyze image. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedFile(null);
    setImagePreview(null);
    setAnalysisResult(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      <Toaster position="top-right" />

      {/* Header */}
      <header className="sticky top-0 z-50 backdrop-blur-xl bg-slate-900/80 border-b border-slate-700/50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center gap-3">
              <div className="text-3xl">🧬</div>
              <div>
                <h1 className="text-xl font-bold text-white">Tongue AI Health Analyzer</h1>
                <p className="text-xs text-slate-400">AI-powered oral health diagnostic system</p>
              </div>
            </div>
            {healthStatus && (
              <div className="flex items-center gap-2 px-4 py-2 bg-emerald-500/10 rounded-lg border border-emerald-500/30">
                <div className="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div>
                <span className="text-sm font-medium text-emerald-400">API Connected</span>
              </div>
            )}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {!analysisResult ? (
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Upload Section */}
            <div className="lg:col-span-2">
              <div className="bg-slate-800/50 backdrop-blur border border-slate-700/50 rounded-2xl p-8 hover:border-slate-600/50 transition-all">
                <ImageUpload onImageSelect={handleImageSelect} isLoading={isLoading} />

                {imagePreview && (
                  <div className="mt-8 mb-8">
                    <p className="text-sm text-slate-400 mb-4">Image Preview</p>
                    <div className="relative rounded-xl overflow-hidden shadow-2xl border border-slate-700/50">
                      <img src={imagePreview} alt="Preview" className="w-full h-auto" />
                    </div>
                  </div>
                )}

                <div className="flex gap-4 justify-center pt-6 border-t border-slate-700/50">
                  <button
                    onClick={handleAnalyze}
                    disabled={!selectedFile || isLoading}
                    className="px-8 py-3 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold rounded-lg disabled:from-slate-600 disabled:to-slate-700 disabled:cursor-not-allowed transition-all duration-200 flex items-center gap-2 shadow-lg hover:shadow-blue-500/50"
                  >
                    {isLoading ? (
                      <>
                        <Spinner />
                        <span>Analyzing...</span>
                      </>
                    ) : (
                      <>
                        <span>⚡</span>
                        <span>Analyze Image</span>
                      </>
                    )}
                  </button>
                  {selectedFile && (
                    <button
                      onClick={handleReset}
                      disabled={isLoading}
                      className="px-8 py-3 bg-slate-700 hover:bg-slate-600 text-slate-100 font-semibold rounded-lg disabled:cursor-not-allowed transition-all duration-200"
                    >
                      Clear
                    </button>
                  )}
                </div>
              </div>
            </div>

            {/* Info Sidebar */}
            <div className="space-y-4">
              <div className="bg-gradient-to-br from-blue-600/20 to-cyan-600/20 border border-blue-500/30 rounded-2xl p-6 backdrop-blur">
                <h3 className="text-lg font-semibold text-blue-300 mb-3">How it works</h3>
                <ul className="space-y-2 text-sm text-slate-300">
                  <li className="flex gap-2">
                    <span className="text-blue-400">1.</span>
                    <span>Upload tongue image</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-400">2.</span>
                    <span>AI analyzes patterns</span>
                  </li>
                  <li className="flex gap-2">
                    <span className="text-blue-400">3.</span>
                    <span>Get health insights</span>
                  </li>
                </ul>
              </div>

              <div className="bg-gradient-to-br from-amber-600/10 to-orange-600/10 border border-amber-500/30 rounded-2xl p-6 backdrop-blur">
                <h3 className="text-sm font-semibold text-amber-300 mb-2">📋 Requirements</h3>
                <p className="text-xs text-slate-400">JPG, PNG formats • Clear image • Good lighting</p>
              </div>
            </div>
          </div>
        ) : (
          <div>
            <ResultsDisplay data={analysisResult} imagePreview={imagePreview} />
            <div className="text-center mt-12">
              <button
                onClick={handleReset}
                className="px-8 py-3 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold rounded-lg transition-all duration-200 shadow-lg hover:shadow-blue-500/50"
              >
                ↻ Analyze Another Image
              </button>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-slate-700/50 mt-20 py-8">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-sm text-slate-400 mb-2">
            ⚠️ <strong>Disclaimer:</strong> For informational purposes only. Not a substitute for professional medical diagnosis.
          </p>
          <p className="text-xs text-slate-500">Powered by Advanced AI & Computer Vision</p>
        </div>
      </footer>
    </div>
  );
}

const Spinner = () => (
  <svg
    className="w-5 h-5 animate-spin"
    fill="none"
    viewBox="0 0 24 24"
    stroke="currentColor"
  >
    <circle cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="2" opacity="0.2" />
    <path fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
  </svg>
);

export default App;
