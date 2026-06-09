import React from 'react';

const ScoreCard = ({ label, score, maxScore = 100, icon, color = 'blue' }) => {
  const percentage = Math.min((score / maxScore) * 100, 100);
  let bgColor = 'from-emerald-600/20 to-green-600/20 border-emerald-500/30';
  let textColor = 'text-emerald-300';

  if (percentage < 60) {
    bgColor = 'from-red-600/20 to-rose-600/20 border-red-500/30';
    textColor = 'text-red-300';
  } else if (percentage < 80) {
    bgColor = 'from-amber-600/20 to-yellow-600/20 border-amber-500/30';
    textColor = 'text-amber-300';
  }

  return (
    <div className={`bg-gradient-to-br ${bgColor} border rounded-xl p-6 backdrop-blur hover:border-opacity-100 transition-all duration-300`}>
      <div className="text-3xl mb-3">{icon}</div>
      <p className="text-sm text-slate-400 mb-2">{label}</p>
      <div className={`text-4xl font-bold ${textColor}`}>{score.toFixed(1)}</div>
      <div className="w-full bg-slate-700/50 rounded-full h-2 mt-4">
        <div
          className={`h-2 rounded-full transition-all duration-300 ${
            percentage >= 80
              ? 'bg-gradient-to-r from-emerald-500 to-green-400'
              : percentage >= 60
              ? 'bg-gradient-to-r from-amber-500 to-yellow-400'
              : 'bg-gradient-to-r from-red-500 to-rose-400'
          }`}
          style={{ width: `${percentage}%` }}
        ></div>
      </div>
    </div>
  );
};

const AnalysisCard = ({ title, icon, children }) => (
  <div className="bg-slate-800/50 backdrop-blur border border-slate-700/50 rounded-xl p-6 hover:border-slate-600/50 transition-all duration-300">
    <div className="flex items-center gap-2 mb-4">
      <span className="text-2xl">{icon}</span>
      <h3 className="text-lg font-semibold text-white">{title}</h3>
    </div>
    <div className="text-slate-300">{children}</div>
  </div>
);

const ResultsDisplay = ({ data, imagePreview }) => {
  if (!data) return null;

  const nutritionScore = data.NutritionScore || 0;
  const mantleScore = data.MantleScore || 0;
  const jaggedness = data.Jaggedness || 0;
  const redness = data.redness || 0;
  const summary = data.Summary || 'AI summary temporarily unavailable. Please try again later.';

  return (
    <div className="space-y-8 pb-8">
      {/* Main Score Card */}
      <div className="bg-gradient-to-br from-slate-800 to-slate-900 border border-slate-700/50 rounded-2xl p-8 backdrop-blur shadow-2xl">
        <div className="text-center">
          <p className="text-slate-400 text-lg mb-2">Overall Health Score</p>
          <div className="text-7xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent mb-2">
            {nutritionScore.toFixed(0)}
          </div>
          <p className="text-slate-400 mb-6">Nutrition & Health Index</p>

          {/* Main Score Bar */}
          <div className="max-w-xs mx-auto mb-4">
            <div className="w-full bg-slate-700/50 rounded-full h-4">
              <div
                className={`h-4 rounded-full transition-all duration-500 ${
                  nutritionScore >= 75
                    ? 'bg-gradient-to-r from-emerald-500 to-green-400'
                    : nutritionScore >= 50
                    ? 'bg-gradient-to-r from-amber-500 to-yellow-400'
                    : 'bg-gradient-to-r from-red-500 to-rose-400'
                }`}
                style={{ width: `${Math.min(nutritionScore, 100)}%` }}
              ></div>
            </div>
          </div>

          <div className="flex justify-around text-sm text-slate-400">
            <span>0</span>
            <span>50</span>
            <span>100</span>
          </div>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <ScoreCard label="Mantle Score" score={mantleScore} icon="🛡️" />
        <ScoreCard label="Jaggedness Score" score={jaggedness} icon="📐" />
        <ScoreCard label="Redness Analysis" score={redness} maxScore={10} icon="🔴" />
      </div>

      {/* Image Preview */}
      {imagePreview && (
        <div className="bg-slate-800/50 backdrop-blur border border-slate-700/50 rounded-xl p-6">
          <p className="text-slate-400 text-sm mb-4">Uploaded Image</p>
          <img src={imagePreview} alt="Analyzed tongue" className="max-w-md mx-auto rounded-lg shadow-lg" />
        </div>
      )}

      {/* Analysis Details Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* White Coating */}
        <AnalysisCard title="White Coating Analysis" icon="⚪">
          <div className="space-y-3">
            <div className="text-2xl font-bold text-white">
              {(data.white_coating?.white_coating_percentage || 0).toFixed(1)}%
            </div>
            <div className="w-full bg-slate-700/50 rounded-full h-3">
              <div
                className={`h-3 rounded-full ${
                  (data.white_coating?.white_coating_percentage || 0) > 20
                    ? 'bg-gradient-to-r from-orange-500 to-red-500'
                    : 'bg-gradient-to-r from-blue-500 to-cyan-500'
                }`}
                style={{ width: `${Math.min(data.white_coating?.white_coating_percentage || 0, 100)}%` }}
              ></div>
            </div>
            <p className="text-sm text-slate-400 mt-2">
              {(data.white_coating?.white_coating_percentage || 0) > 20
                ? '⚠️ High coating detected - May indicate health concerns'
                : '✓ Coating level within normal range'}
            </p>
          </div>
        </AnalysisCard>

        {/* Crack Detection */}
        <AnalysisCard title="Crack Detection" icon="🔍">
          <div className="space-y-3">
            <div className="text-2xl font-bold text-white">
              {(data.Cracks?.score || 0).toFixed(1)} / 10
            </div>
            <div className="w-full bg-slate-700/50 rounded-full h-3">
              <div
                className={`h-3 rounded-full ${
                  (data.Cracks?.score || 0) > 5
                    ? 'bg-gradient-to-r from-orange-500 to-red-500'
                    : 'bg-gradient-to-r from-emerald-500 to-green-400'
                }`}
                style={{ width: `${Math.min((data.Cracks?.score || 0) * 10, 100)}%` }}
              ></div>
            </div>
            <p className="text-sm text-slate-400 mt-2">
              {(data.Cracks?.score || 0) > 5
                ? '⚠️ Significant cracks detected'
                : '✓ Minimal to no cracks detected'}
            </p>
          </div>
        </AnalysisCard>
      </div>

      {/* Papillae Analysis */}
      <AnalysisCard title="Papillae Analysis" icon="🔬">
        <div className="grid grid-cols-3 gap-6">
          <div>
            <p className="text-slate-400 text-sm mb-2">Total Detected</p>
            <p className="text-3xl font-bold text-cyan-400">
              {data.papillae_analysis?.total_papillae || 0}
            </p>
          </div>
          <div>
            <p className="text-slate-400 text-sm mb-2">Average Size</p>
            <p className="text-3xl font-bold text-blue-400">
              {(data.papillae_analysis?.avg_size || 0).toFixed(1)}px
            </p>
          </div>
          <div>
            <p className="text-slate-400 text-sm mb-2">Avg Redness</p>
            <p className="text-3xl font-bold text-rose-400">
              {(data.papillae_analysis?.avg_redness || 0).toFixed(2)}
            </p>
          </div>
        </div>
      </AnalysisCard>

      {/* AI Summary */}
      <div className="bg-gradient-to-br from-blue-600/20 to-cyan-600/20 border border-blue-500/30 rounded-xl p-8 backdrop-blur">
        <div className="flex items-start gap-3">
          <span className="text-3xl">🤖</span>
          <div>
            <h3 className="text-lg font-semibold text-blue-300 mb-3">AI Health Summary</h3>
            <p className="text-slate-300 leading-relaxed">{summary}</p>
            <p className="text-xs text-slate-500 mt-4 italic">
              ⚠️ This analysis is for informational purposes only. Please consult a healthcare professional.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultsDisplay;
