import { Component, OnInit, NgModule } from '@angular/core';

import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { ApiService } from '../api.service';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Router, ActivatedRoute } from '@angular/router';
import { delay } from 'q';


@NgModule({
  imports: [
    // BrowserModule,

    // FormsModule      //<----------make sure you have added this.
  ],
})

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  client : HttpClient
  loginForm: FormGroup;
  submitted = false;
  resok = '';
  constructor(private formBuilder: FormBuilder, private apiService: ApiService, private router: Router, private route: ActivatedRoute) { }
  onFormSubmit() {
  }

  ngOnInit() {    
    this.loginForm = this.formBuilder.group({
        username: ['', Validators.required],
        password: ['', [Validators.required,  Validators.minLength(8)]],    
    });
  }
  // submit() {
   
  // }

    // convenience getter for easy access to form fields
    get f() { return this.loginForm.controls; }

    async onSubmit() {
        this.submitted = true;
        var token;
        // stop here if form is invalid
        if (this.loginForm.invalid) {
            return;
        }
        var json = this.loginForm.value;
        var badrequestlogin = this.apiService.login(JSON.stringify(json));

        console.log('badrequestlogin ', badrequestlogin);

         if (badrequestlogin === false){
        token = this.apiService.getToken();

        if(token !== null){
          this.router.navigate(['expense'])
          console.log('login  if ', token)
        }else{
          console.log('login else ', token)
          var n:number = 1;
          while(n <= 5){
            if(token = this.apiService.getToken()!== null){
              break
            }
            await delay(200);
            n++;
          }
          if(this.apiService.getToken() !== null){

            this.router.navigate(['expense'])
          }
          return;
        
        }
      } else{
        return;
      }
        // if( this.apiService.login(JSON.stringify(json)) === false){
        //   this.router.navigate(['expense'])
        // }else{
        //   return;
        // }
        // console.log(this.apiService.headers);
        // console.log( this.apiService.login);

 

    }

}
