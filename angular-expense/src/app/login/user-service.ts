import { Injectable } from '@angular/core';
import { User } from './user';

@Injectable()
export class UserService {
   createUser(user: User) {
     console.log('Email: ' + user.email);
     console.log('password: ' + user.password);
   }
}
