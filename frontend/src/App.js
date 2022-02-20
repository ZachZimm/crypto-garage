import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';
// import axios from 'axios'
import $ from 'jquery'

function App() {
	const [message, setMessage] = useState({})
	const query = async () => {
		var request = '/flask/hello' // This should be passed in as an arg
		var uri = 'http://127.0.0.1:5000' + request
		console.log(uri)
		
		$.getJSON(uri, function(data){
			console.log("Response: ", data)
			setMessage(data)
		})
	}
// query()
	useEffect(()=>{
		query()
//		axios.get('http://localhost:5000/flask/hello').then(response => {
//			console.log("Success!", response)
//			setMessage(response)
//		}).catch(error => {
//			console.log(error)
//		})
	}, [])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          React + Flask = (this)
        </p>
		<h3>{message.message}</h3> 
      </header>
    </div>
  );
}

export default App;
