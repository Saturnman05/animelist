import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';

import { environment } from '../../../environments/environment';
import { TokenService } from '../token/token.service';
import { User } from '../../models/user.model';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  private readonly API_URL = `${environment.apiUrl}/users`;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  private http = inject(HttpClient);
  private tokenService = inject(TokenService);
  constructor() {
    this.isAuthenticatedSubject.next(this.tokenService.isLoggedIn());
  }

  getMyUser(): Observable<User> {
    return this.http.get<User>(`${this.API_URL}/my_user`, {
      headers: {
        'Content-type': 'application/json',
        Authorization: `Bearer ${this.tokenService.getToken()}`,
      },
    });
  }
}
