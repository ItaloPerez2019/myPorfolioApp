import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';

import { FormsModule }   from '@angular/forms';

import { RouterModule, Routes } from '@angular/router';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { NavBarComponent } from './nav-bar/nav-bar.component';

import { ReactiveFormsModule } from '@angular/forms';
import { UserRegistrationComponent } from './user-registration/user-registration.component';

import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { FooterComponent } from './footer/footer.component';
import { ExpenseComponent } from './expense/expense.component';
import { LogoutComponent } from './logout/logout.component';



@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    PageNotFoundComponent,
    NavBarComponent,
    UserRegistrationComponent,
    FooterComponent,
    ExpenseComponent,
    LogoutComponent
  ],
  imports: [
    AppRoutingModule,
    // RouterModule.forRoot(
    //   { enableTracing: true } // <-- debugging purposes only
    // ),
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
