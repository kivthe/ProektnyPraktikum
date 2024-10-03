import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MoreCars = () => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3001/data'); // Замените на URL вашего JSON файла
        setImages(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      {images.map(img => (
        <img key={img.id} src={img.image} alt={img.title} />
      ))}
    </div>
  );
};

export default MoreCars;
