import React, { useState } from 'react';

const UserForm = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault(); // Impede o comportamento padrão do formulário

    // Cria o FormData com os dados do formulário
    const formData = new FormData();
    formData.append('username', username);
    formData.append('email', email);
    formData.append('password', password);

    try {
      // Faz o POST request usando fetch
      const response = await fetch('/api/create_user/', {
        method: 'POST',
        headers: {
          'Authorization': 'Basic ' + btoa('smart_user:123456') // Autenticação básica
        },
        body: formData
      });

      if (response.ok) {
        // Se a resposta for ok, exibe a mensagem de sucesso
        alert('Usuário cadastrado com sucesso!');
      } else {
        throw new Error('Erro ao cadastrar usuário');
      }
    } catch (error) {
      console.error('Erro:', error);
      alert('Erro ao cadastrar usuário');
    }
  };

  return (
    <div>
      <h2>Cadastrar Novo Usuário</h2>
      <form onSubmit={handleSubmit} id="userForm">
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Cadastrar</button>
      </form>
    </div>
  );
};

export default UserForm;
