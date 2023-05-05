import { Component, ViewChild, ElementRef } from '@angular/core';
import {MatIconModule} from '@angular/material/icon';
import {
  FormGroup,
  FormControl,
  Validators,
  FormArray,
  FormBuilder,
} from '@angular/forms';
import { BackendServiceService } from './../_services/backend-service.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  @ViewChild('scrollMe') private chatScrollContainer: ElementRef<any>;
  messages: any = [];
  chatForm: FormGroup;
  showMic:Boolean = false;
  public isUserSpeaking: boolean = false;
  isStoppedSpeechRecog = false;

  constructor(
    public formBuilder: FormBuilder,
    public backend: BackendServiceService
  ) {
    this.chatForm = this.formBuilder.group({
      message: ['', Validators.required],
    });
    this.messages.push({
      // text: 'Hello, My Name is Jarvis, How can I help you?',
      text: 'Hi,I am your HR Helpdesk Augmented Assistant.\n Here are the things you can do with the assistant\n1 - Apply Leave \n2 - Check In \n3 - Check Out',
      image: '',
      from: 'bot',
      time: new Date().toDateString(),
    });
  }

  onSubmit() {
    this.showMic = false;
    this.messages.push({
      text: this.chatForm.value.message,
      from: 'me',
      time: new Date().toDateString(),
    });
    this.stopRecording();

    this.backend
      .postMethod({ message: this.chatForm.value.message })
      .subscribe((response: any) => {
        console.log(response);
        this.chatForm.reset();
        for (let index = 0; index < response.length; index++) {
          this.messages.push({
            text: response[index].text,
            image: response[index].image,
            from: 'bot',
            time: new Date().toDateString(),
          });
          this.backend.readText(response[index].text);
          this.scrollToBottom();
        }
      });
    console.log(this.messages);
  }

  ngOnInit(): void {
    this.initVoiceInput();
    this.scrollToBottom();
    this.backend.readText('Hi,I am your HR Helpdesk Augmented Assistant.\n Here are the things you can do with the assistant\n1 - Apply Leave\n2 - Check In \n3 - Check Out');
  }

  ngAfterViewChecked() {
    this.scrollToBottom();
  }

  scrollToBottom(): void {
    try {
      this.chatScrollContainer.nativeElement.scrollTop =
        this.chatScrollContainer.nativeElement.scrollHeight;
    } catch (err) {}
  }

  /**
   * @description Function to stop recording.
   */
  stopRecording() {
    this.backend.stop();
    this.isUserSpeaking = false;
  }

  /**
   * @description Function for initializing voice input so user can chat with machine.
   */
  initVoiceInput() {
    // Subscription for initializing and this will call when user stopped speaking.
    this.backend.init().subscribe(() => {
      // User has stopped recording
      // Do whatever when mic finished listening
    });

    // Subscription to detect user input from voice to text.
    this.backend.speechInput().subscribe((input) => {
      // Set voice text output to
      this.chatForm.controls['message'].setValue(input);
    });
  }

  /**
   * @description Function to enable voice input.
   */
  startRecording() {
    this.showMic = true;
    this.isUserSpeaking = true;
    this.backend.start();
    this.chatForm.controls['message'].reset();
  }

  /**
   * trying reset
   */
   resetRecording() {
      
    // Reset the form control for message
    this.chatForm.controls['message'].reset();
  
    // Start a new recording
    this.startRecording();
  }
}
