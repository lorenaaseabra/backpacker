import { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMapMarkedAlt, faMapMarkerAlt, faRoute, faTemperatureHigh, faWind } from '@fortawesome/free-solid-svg-icons';

export default function RouteFinder() {
  const [cidades, setCidades] = useState([]);
  const [origem, setOrigem] = useState('');
  const [destino, setDestino] = useState('');
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState('');
  const [descricao, setDescricao] = useState('');
  const [clima, setClima] = useState(null);

  const coordenadas = {
    "Berlim": { lat: 52.52, lon: 13.405 },
    "Viena": { lat: 48.2082, lon: 16.3738 },
    "Bruxelas": { lat: 50.8503, lon: 4.3517 },
    "Praga": { lat: 50.0755, lon: 14.4378 },
    "Paris": { lat: 48.8566, lon: 2.3522 },
    "Atenas": { lat: 37.9838, lon: 23.7275 },
    "Budapeste": { lat: 47.4979, lon: 19.0402 },
    "Roma": { lat: 41.9028, lon: 12.4964 },
    "Lisboa": { lat: 38.7169, lon: -9.1399 },
    "Madrid": { lat: 40.4168, lon: -3.7038 },
  };

  const imagemURLs = {
    "Berlim": "https://images.pexels.com/photos/1128416/pexels-photo-1128416.jpeg",
    "Viena": "https://images.pexels.com/photos/161074/vienna-st-charles-s-church-downtown-church-161074.jpeg?",
    "Bruxelas": "https://images.pexels.com/photos/1595085/pexels-photo-1595085.jpeg",
    "Praga": "https://images.pexels.com/photos/753337/pexels-photo-753337.jpeg",
    "Paris": "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg",
    "Atenas": "https://images.pexels.com/photos/31411936/pexels-photo-31411936/free-photo-of-partenon.jpeg",
    "Budapeste": "https://images.pexels.com/photos/31340477/pexels-photo-31340477.jpeg",
    "Roma": "https://images.pexels.com/photos/2064827/pexels-photo-2064827.jpeg",
    "Lisboa": "https://images.pexels.com/photos/1534560/pexels-photo-1534560.jpeg",
    "Madrid": "https://images.pexels.com/photos/930595/pexels-photo-930595.jpeg"
  };

  useEffect(() => {
    axios.get('http://localhost:8001/cidades')
      .then(res => setCidades(res.data))
      .catch(() => setErro('Erro ao buscar cidades.'));
  }, []);

  const buscarRota = async () => {
    if (!origem || !destino || origem === destino) {
      setErro('Selecione cidades diferentes.');
      setResultado(null);
      return;
    }

    try {
      const rotaRes = await axios.post('http://localhost:8001/rota', { origem, destino });
      setResultado(rotaRes.data);
      setErro('');

      const cidadeFinal = rotaRes.data.caminho.at(-1);

      const wikiRes = await axios.get(`https://pt.wikipedia.org/api/rest_v1/page/summary/${cidadeFinal}`);
      setDescricao(wikiRes.data.extract);

      const { lat, lon } = coordenadas[cidadeFinal];
      const weatherRes = await axios.get(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`);
      setClima(weatherRes.data.current_weather);

    } catch (err) {
      setErro('Erro ao buscar rota ou informações externas.');
      setResultado(null);
    }
  };

  return (
    <div className="min-h-screen bg-light text-dark">
      <div className="position-relative" style={{ height: '500px', overflow: 'hidden' }}>
        <div id="headerCarousel" className="carousel slide carousel-fade h-100" data-bs-ride="carousel" data-bs-interval="4000">
          <div className="carousel-inner h-100">
            {cidades.map((cidade, index) => (
              <div key={cidade} className={`carousel-item h-100 ${index === 0 ? 'active' : ''}`}>
                <img
                  src={imagemURLs[cidade]}
                  className="d-block w-100 h-100 position-absolute top-0 start-0"
                  alt={`Imagem de ${cidade}`}
                  style={{ objectFit: 'cover', zIndex: 1 }}
                />
              </div>
            ))}
          </div>
        </div>

        <div className="position-absolute top-50 start-50 translate-middle text-center w-100 px-3" style={{ zIndex: 2 }}>
          <h1 className="display-3 fw-bold text-white">
            <FontAwesomeIcon icon={faMapMarkedAlt} className="me-2" /> Backpacker
          </h1>
          <p className="lead text-white mt-2">
            Explore rotas, encontre destinos, viva aventuras.
          </p>
        </div>
      </div>
      <div className="container py-5">
        {erro && <div className="alert alert-danger text-center mb-4 fw-semibold">{erro}</div>}

        <div className="d-flex flex-wrap justify-content-center gap-4 mb-4">
          <div>
            <label className="fw-semibold mb-2">
              <FontAwesomeIcon icon={faMapMarkerAlt} className="me-2" /> Origem
            </label>
            <select
              className="form-select"
              value={origem}
              onChange={e => setOrigem(e.target.value)}
            >
              <option value="">Selecione a cidade</option>
              {cidades.map(cidade => <option key={cidade} value={cidade}>{cidade}</option>)}
            </select>
          </div>

          <div>
            <label className="fw-semibold mb-2">
              <FontAwesomeIcon icon={faMapMarkerAlt} className="me-2" /> Destino
            </label>
            <select
              className="form-select"
              value={destino}
              onChange={e => setDestino(e.target.value)}
            >
              <option value="">Selecione a cidade</option>
              {cidades.map(cidade => <option key={cidade} value={cidade}>{cidade}</option>)}
            </select>
          </div>
        </div>

        <div className="text-center">
          <button
            onClick={buscarRota}
            className="btn btn-dark px-5 py-2"
          >
            <FontAwesomeIcon icon={faRoute} className="me-2" /> Encontrar Melhor Rota
          </button>
        </div>

        {resultado && (
          <div className="mt-5 bg-white p-4 rounded shadow text-center">
            <h2 className="display-5 fw-bold mb-3 text-dark">Melhor Rota</h2>
            <p className="fs-5 mb-2">{resultado.caminho.join(' → ')}</p>
            <p className="fw-semibold fs-6 mb-4">Distância Total: {resultado.distancia} km</p>
            <img
              src={`./images/${resultado.caminho.at(-1)}.jpg`}
              alt={`Imagem de ${resultado.caminho.at(-1)}`}
              className="img-fluid rounded shadow"
              style={{ maxHeight: '300px', objectFit: 'cover' }}
            />

            {descricao && (
              <div className="text-start mt-4">
                <h5 className="fw-bold">Sobre {resultado.caminho.at(-1)}</h5>
                <p>{descricao}</p>
              </div>
            )}

            {clima && (
              <div className="bg-light rounded p-3 shadow-sm text-start mt-4 mx-auto" style={{ maxWidth: '300px' }}>
                <h6 className="fw-bold mb-3">Clima atual</h6>
                <p><FontAwesomeIcon icon={faTemperatureHigh} className="me-2 text-danger" /> Temperatura: {clima.temperature}°C</p>
                <p><FontAwesomeIcon icon={faWind} className="me-2 text-info" /> Vento: {clima.windspeed} km/h</p>
              </div>
            )}

            <div className="bg-light rounded p-3 shadow-sm mt-4" style={{ width: '100%', maxWidth: '800px', margin: '0 auto' }}>
              <h6 className="fw-bold mb-3">Localização</h6>
              <iframe
                title="Mapa"
                width="100%"
                height="350"
                style={{ border: 0 }}
                loading="lazy"
                allowFullScreen
                src={`https://www.google.com/maps?q=${resultado.caminho.at(-1)}&output=embed`}
              ></iframe>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}