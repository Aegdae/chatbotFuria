import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})

export class ChatService {

  // URL do backend para comunicação com o servidor de chat

  private apiUrl = 'http://localhost:5000/chat';

  constructor(private http: HttpClient) {}

  // Método para enviar uma mensagem ao backend com o histórico da conversa

  sendMessage(message: string, history: { role: string; message: string }[]) {
    return this.http.post<{ response: string}>(this.apiUrl, {
      message,
      history
    });
  }
}
