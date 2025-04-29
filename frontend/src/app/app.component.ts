import { Component, ElementRef, ViewChild, AfterViewInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ChatService } from './services/chat.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  imports: [FormsModule, CommonModule]

})


export class AppComponent implements AfterViewInit {
  userInput:string = '';
  responseText: string = ''
  messages: {sender: string, text: string}[] = []

  @ViewChild('chatMessages') chatContainer!: ElementRef;


  // Salvar as conversar enquanto a aba não e fechada
  ngOnInit() {
    if (typeof window !== 'undefined' ) {
      let userId = sessionStorage.getItem('userId')
      if (!userId) {
        userId = this.generateUniqueId();
        sessionStorage.setItem('userId', userId)
      }

      const savedMessages = sessionStorage.getItem('messages');
      if (savedMessages) {
        this.messages = JSON.parse(savedMessages);
      }
    }
  }

  // Gerar ID para salvar a conversa
  generateUniqueId(): string {
    return 'user_' + Math.random().toString(36).substr(2, 9)
  }


  constructor(private chatService: ChatService){}


  sendMessage(event: Event) {
    event.preventDefault();
    const typing = document.getElementById("typing");

    if (!this.userInput.trim()) return;

    this.messages.push({ sender: 'Usuario', text: this.userInput });

    if (typeof window !== 'undefined') {
      sessionStorage.setItem('message', JSON.stringify(this.messages))
    }

    if (typing) typing.classList.add("show");

    const lastMessages = this.messages.slice(-5);
    const context = this.messages.map( msg => ({
      role: msg.sender === 'Usuario' ? 'USER': 'CHATBOT',
      message: msg.text
    }));
    const contextMessages = `${context}\nUsuario: ${this.userInput}`



    this.chatService.sendMessage(this.userInput, context).subscribe({
      next: (res) => {
        this.responseText = res.response;
        if (typing) typing.classList.remove("show");
        this.messages.push({ sender: 'IA Furia', text: this.responseText });
        if (typeof window !== 'undefined'){
          sessionStorage.setItem('messages', JSON.stringify(this.messages));
        }
        setTimeout(() => this.scrollToBottom(), 10)
      },
      error: (err) => {
        this.responseText = 'Erro ao enviar mensagem';
        if (typing) typing.classList.remove("show");
        this.messages.push({ sender: 'Bot', text: this.responseText });
        if (typeof window !== 'undefined') {
          sessionStorage.setItem('messages', JSON.stringify(this.messages));
        }
        
        setTimeout(() => this.scrollToBottom(), 10)
        console.error('Erro na requisição:', err);
      }
    });

    this.userInput = '';
  }

  // Descer a conversa a cada nova interação

  private scrollToBottom(): void {
    if (this.chatContainer) {
      try {
        this.chatContainer.nativeElement.scrollTop = this.chatContainer.nativeElement.scrollHeight;
      } catch (err) {
        console.error('Erro ao rolar:', err);
      }
    }
  }


  ngAfterViewInit(): void {
    this.scrollToBottom();
  }
}

