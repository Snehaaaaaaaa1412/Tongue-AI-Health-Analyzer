import React, { useRef } from 'react';

const ImageUpload = ({ onImageSelect, isLoading }) => {
  const fileInputRef = useRef(null);

  const handleDragOver = (e) => {
    e.preventDefault();
    e.currentTarget.classList.add('border-blue-500', 'bg-blue-500/10');
  };

  const handleDragLeave = (e) => {
    e.currentTarget.classList.remove('border-blue-500', 'bg-blue-500/10');
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.currentTarget.classList.remove('border-blue-500', 'bg-blue-500/10');
    
    const files = e.dataTransfer.files;
    if (files.length > 0) {
      const file = files[0];
      if (file.type.startsWith('image/')) {
        onImageSelect(file);
      } else {
        alert('Please drop an image file');
      }
    }
  };

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];
    if (file && file.type.startsWith('image/')) {
      onImageSelect(file);
    } else {
      alert('Please select an image file');
    }
  };

  return (
    <div className="mb-8">
      <div
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className="border-2 border-dashed border-slate-600 hover:border-blue-500 bg-slate-700/20 hover:bg-blue-500/10 rounded-xl p-12 text-center cursor-pointer transition-all duration-300"
      >
        <div className="flex justify-center mb-4">
          <svg
            className="w-16 h-16 text-slate-400 group-hover:text-blue-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M12 4v16m8-8H4"
            />
          </svg>
        </div>
        <p className="text-slate-200 text-lg font-medium mb-2">
          Drag your tongue image here
        </p>
        <p className="text-slate-400 text-sm mb-4">or click to browse from your device</p>
        <p className="text-slate-500 text-xs">Supported formats: JPG, PNG, GIF • Max 50MB</p>
      </div>
      <input
        ref={fileInputRef}
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="hidden"
        disabled={isLoading}
      />
    </div>
  );
};

export default ImageUpload;
