import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, tap } from 'rxjs';

import { environment } from '../../../environments/environment';
import { LoginRequest } from '../../models/login-request.model';
import { LoginResponse } from '../../models/login-response.model';
import { TokenService } from '../token/token.service';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly API_URL = `${environment.apiUrl}/auth`;
  private isAuthenticatedSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.isAuthenticatedSubject.asObservable();

  constructor(private http: HttpClient, private tokenService: TokenService) {
    // Check if the user is already logged in when the service is initialized
    this.isAuthenticatedSubject.next(this.tokenService.isLoggedIn());
  }

  login(credentials: LoginRequest): Observable<LoginResponse> {
    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password', credentials.password);

    const headers = new HttpHeaders({
      'Content-type': 'application/x-www-form-urlencoded',
    });

    return this.http
      .post<LoginResponse>(`${this.API_URL}/login`, body.toString(), {
        headers,
      })
      .pipe(
        tap((response) => {
          this.tokenService.saveToken(response.access_token);
          this.isAuthenticatedSubject.next(true);
        })
      );
  }

  logout(): void {
    this.tokenService.clear();
    this.isAuthenticatedSubject.next(false);
  }

  refreshToken(): Observable<{ accessToken: string }> {
    return this.http
      .post<{ accessToken: string }>(`${this.API_URL}/refresh-token`, {})
      .pipe(
        tap((response) => {
          this.tokenService.saveToken(response.accessToken);
        })
      );
  }

  getCurrentUser(): any {
    return this.tokenService.getUser();
  }

  isLoggedIn(): boolean {
    return this.tokenService.isLoggedIn();
  }
}
