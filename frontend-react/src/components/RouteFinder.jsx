import { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMapMarkedAlt, faMapMarkerAlt, faRoute } from '@fortawesome/free-solid-svg-icons';

export default function RouteFinder() {
  const [cidades, setCidades] = useState([]);
  const [origem, setOrigem] = useState('');
  const [destino, setDestino] = useState('');
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState('');

  useEffect(() => {
    axios.get('http://localhost:8001/cidades')
      .then(res => setCidades(res.data))
      .catch(() => setErro('Erro ao buscar cidades.'));
  }, []);

  const buscarRota = () => {
    if (!origem || !destino || origem === destino) {
      setErro('Selecione cidades diferentes.');
      setResultado(null);
      return;
    }

    axios.post('http://localhost:8001/rota', { origem, destino })
      .then(res => {
        setResultado(res.data);
        setErro('');
      })
      .catch(err => {
        setErro(err.response?.data?.detail || 'Erro ao buscar rota.');
        setResultado(null);
      });
  };

  return (
    <div className="container max-w-xl mx-auto p-5 bg-white rounded-xl shadow-lg">
      <h1 className="text-3xl font-semibold text-gray-700 mb-5 text-center">
        <FontAwesomeIcon icon={faMapMarkedAlt} className="mr-2 text-green-600"/> Backpacker
      </h1>

      {erro && <div className="alert alert-danger text-center">{erro}</div>}

      <div className="flex flex-col md:flex-row justify-between gap-3">
        <div className="w-full">
          <label className="font-medium text-gray-700">
            <FontAwesomeIcon icon={faMapMarkerAlt} /> Origem
          </label>
          <select 
            className="form-select mt-1"
            value={origem}
            onChange={e => setOrigem(e.target.value)}
          >
            <option value="">Selecione...</option>
            {cidades.map(cidade => <option key={cidade} value={cidade}>{cidade}</option>)}
          </select>
        </div>

        <div className="w-full">
          <label className="font-medium text-gray-700">
            <FontAwesomeIcon icon={faMapMarkerAlt} /> Destino
          </label>
          <select 
            className="form-select mt-1"
            value={destino}
            onChange={e => setDestino(e.target.value)}
          >
            <option value="">Selecione...</option>
            {cidades.map(cidade => <option key={cidade} value={cidade}>{cidade}</option>)}
          </select>
        </div>
      </div>

      <button 
        onClick={buscarRota}
        className="btn btn-dark mt-4 w-full"
      >
        <FontAwesomeIcon icon={faRoute} className="mr-2"/> Encontrar Melhor Rota
      </button>

      {resultado && (
        <div className="mt-4 bg-gray-100 p-4 rounded-lg text-center">
          <h2 className="font-semibold text-xl text-gray-800">Melhor Rota</h2>
          <p className="mt-2 text-gray-700">{resultado.caminho.join(' → ')}</p>
          <p className="mt-2 text-gray-700 font-medium">Distância Total: {resultado.distancia} km</p>
        </div>
      )}
    </div>
  )
}
