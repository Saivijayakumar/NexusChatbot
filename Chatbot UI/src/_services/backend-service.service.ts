import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
declare var webkitSpeechRecognition: any;
declare var SpeechSynthesisUtterance: any;
import { Subject } from 'rxjs';
@Injectable({
  providedIn: 'root',
})
export class BackendServiceService {
  recognition: any;
  speech: any;
  isStoppedSpeechRecog = false;
  public text = '';
  private voiceToTextSubject: Subject<string> = new Subject();
  private speakingPaused: Subject<any> = new Subject();
  private tempWords: string = '';

  constructor(private http: HttpClient) {}

  postMethod(params: any) {
    return this.http.post('http://localhost:5002/webhooks/rest/webhook', {
      // return this.http.post('http://localhost:3000/gpt', {
      ...params,
    });
  }

  speechInput() {
    return this.voiceToTextSubject.asObservable();
  }
  readText(text: String) {
    this.speech = new SpeechSynthesisUtterance();
    this.speech.text = text;
    this.speech.rate = 0.99;
    this.speech.pitch = 1;
    window.speechSynthesis.speak(this.speech);
  }

  init() {
    this.recognition = new webkitSpeechRecognition();

    this.recognition.interimResults = true;
    this.recognition.lang = 'en-US';

    this.recognition.addEventListener('result', (e: any) => {
      const transcript = Array.from(e.results)
        .map((result: any) => result[0])
        .map((result) => result.transcript)
        .join('');
      this.tempWords = transcript;
      this.voiceToTextSubject.next(this.text || transcript);
    });
    return this.initListeners();
  }

  initListeners() {
    this.recognition.addEventListener('end', (condition: any) => {
      this.recognition.stop();
    });
    return this.speakingPaused.asObservable();
  }

  start() {
    this.text = '';
    this.isStoppedSpeechRecog = false;
    this.recognition.start();
    this.recognition.addEventListener('end', (condition: any) => {
      if (this.isStoppedSpeechRecog) {
        this.recognition.isActive = true;
        this.recognition.stop();
      } else {
        this.isStoppedSpeechRecog = false;
        this.wordConcat();
        if (
          !this.recognition.lastActiveTime ||
          Date.now() - this.recognition.lastActive > 200
        ) {
          this.recognition.start();
          this.recognition.lastActive = Date.now();
        }
      }
      this.voiceToTextSubject.next(this.text);
    });
  }

  wordConcat() {
    this.text = this.text.trim() + ' ' + this.tempWords;
    this.text = this.text.trim();
    this.tempWords = '';
  }

  stop() {
    this.text = '';
    this.isStoppedSpeechRecog = true;
    this.wordConcat();
    this.recognition.stop();
    this.recognition.isActive = false;
    this.speakingPaused.next('Stopped speaking');
  }
}
