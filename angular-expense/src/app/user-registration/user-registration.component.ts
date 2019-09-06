import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


import { MustMatch } from './_helpers/must-match.validator';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-user-registration',
  templateUrl: './user-registration.component.html',
  styleUrls: ['./user-registration.component.css']
})
export class UserRegistrationComponent implements OnInit {

  registerForm: FormGroup;
    submitted = false;
    emailPattern = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$";
    unamePattern = "^[a-z0-9_-]{8,15}$"; 
    passwordPattern = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).*$";
    constructor(private formBuilder: FormBuilder, private apiService: ApiService) { }

    ngOnInit() {
    
        this.registerForm = this.formBuilder.group({
            username: ['', Validators.required],

            email: ['', [Validators.required, Validators.email]],
            //email: ['', [Validators.required, Validators.pattern(this.emailPattern)]],
            password: ['', [Validators.required,  Validators.minLength(8)]],
            confirmPassword: ['', Validators.required]
        }, {
            validator: MustMatch('password', 'confirmPassword')
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;

        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }
        var json = this.registerForm.value;
        var key = "confirmPassword";
        delete json[key];
        this.apiService.register(JSON.stringify(json));

    }

}
