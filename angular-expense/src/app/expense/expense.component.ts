import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from '../api.service';


@Component({
  selector: 'app-expense',
  templateUrl: './expense.component.html',
  styleUrls: ['./expense.component.css']
})
export class ExpenseComponent implements OnInit {
 
  ngOnInit() {
  }

  private expense  = []; 
  private expenseObservable : Observable<any[]>; 
  constructor(private apiService: ApiService) {
    //this.expenseObservable = this.apiService.get_expense();
    this.apiService.get_expense();
    }
  }


