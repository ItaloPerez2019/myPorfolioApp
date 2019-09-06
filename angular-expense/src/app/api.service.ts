import { Injectable, NgModule, Inject, ErrorHandler } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap, isEmpty } from 'rxjs/operators';
import { Router, ActivatedRoute } from '@angular/router';


@NgModule({
imports:[
  // AppRoutingModule,
]
})

@Injectable({
  providedIn: 'root'
})

export class ApiService {
  // API_KEY = 'YOUR_API_KEY';
  //constructor(private httpClient: HttpClient) {  }
  // public router: Router
  public headers: HttpHeaders;
  private res: any;
  private tokenapp: any;
  private badRequest: boolean = false;
  returnUrl: string;
  url = '';
 

    constructor(private router: Router, private httpClient: HttpClient, private route: ActivatedRoute) {
        this.httpClient = httpClient;
        this.headers = new HttpHeaders();
        // this.headers.append('Accept', 'application/json');
        this.headers.append('Content-Type', 'application/json');
        
    }

    ngOnInit() {
 

      // get return url from route parameters or default to '/'
      this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
    }

  public register(body){
    this.url = 'http://127.0.0.1:8000/api/user/';

    return this.httpClient.post( this.url, body, {headers: new HttpHeaders({ 'Content-Type' :	'application/json'})}) .pipe(
      catchError(err => of([]))
  )
  .subscribe(
      res =>  this.router.navigate(['expense']),
      err => console.log('HTTP Error', err),
      () => console.log('HTTP request completed.')
    );
  }

  public login(body){
    var badRequest: boolean = false
    this.url = 'http://127.0.0.1:8000/api/login/';

   this.httpClient.post( this.url, body, {headers: new HttpHeaders({ 'Content-Type' :	'application/json'})}) .pipe(
      catchError(err => of([]))
  )
  .subscribe(
      res => {
        if(res === undefined || Array.isArray(res) ){
          this.badRequest = true;
        
      }else{
        this.saveTocen(JSON.stringify(res));
      };
      
        console.log('HTTP response---------------', res); },
      // res => console.log('HTTP response', res),
      err => {this.badRequest = true;
            console.log('Error -----------------',err) },
      () => console.log('HTTP request completed.')

    );
    return this.badRequest;
  }

  logout(){
    // this.url='http://127.0.0.1:8000/api-auth/logout/?next=/api/logout/';
    this.url = 'http://127.0.0.1:8000/api/logout/';
    this.httpClient.get( this.url, {headers: new HttpHeaders({ 'Content-Type' :	'application/json'})}) .pipe(
      catchError(err => of([]))
  )
  .subscribe(
      // res => console.log('HTTP response', res),
      res => this.res =  this.saveTocen(res).subscribe(() => {
        // Done
      }, () => {
        // Error
      }),
      // err => console.log('HTTP Error', err),
      err => this.res =  this.errorTocen(err),
      () => console.log('HTTP request completed.')
    );

    return this.res;
  }

  get_expense(){
    // token = this.getToken()
    const headers = new HttpHeaders().set('Content-Type', 'application/json')
    .append('Access-Control-Allow-Origin', '*')
    .append('Authorization', this.getToken())
    .append('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    this.url = 'http://127.0.0.1:8000/api/expense/';
    if (this.getToken() !== null){
      console.log('if -->  ',this.getToken());
    }else{
      console.log('else -->  ',this.getToken());
      this.router.navigate(['login']);
    }

  }

  public getToken(): string {

    return localStorage.getItem('appkey');
  }

  private saveTocen(res:any){
    localStorage.setItem('appkey', res);
    return res
  }

  private errorTocen(err:any){
    localStorage.removeItem('appkey');
  }
}
