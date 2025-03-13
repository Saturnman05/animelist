import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../../environments/environment';
import { TokenService } from '../token/token.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class JikanAnimeService {
  private readonly API_URL = `${environment.jikanApiUrl}/anime`;

  constructor(private http: HttpClient, private tokenService: TokenService) {}

  getAnimes(): Observable<any> {
    return this.http.get(this.API_URL);
  }
}
