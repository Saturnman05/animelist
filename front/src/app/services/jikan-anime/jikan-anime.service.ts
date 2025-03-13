import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../../environments/environment';
import { TokenService } from '../token/token.service';
import { firstValueFrom, map, Observable } from 'rxjs';
import { Anime, JikanAnime, JikanResponse } from '../../models/anime.model';

@Injectable({
  providedIn: 'root',
})
export class JikanAnimeService {
  private readonly API_URL = `${environment.jikanApiUrl}/anime`;

  constructor(private http: HttpClient, private tokenService: TokenService) {}

  async getAllAnimes(): Promise<JikanResponse> {
    let page = 2;
    let hasNextPage = true;
    let response: JikanResponse;

    response = await firstValueFrom(this.http.get<JikanResponse>(this.API_URL));

    while (hasNextPage === true) {
      let newResponse = await firstValueFrom(
        this.http.get<JikanResponse>(`${this.API_URL}?page=${page}`)
      );

      newResponse.data.forEach((anime) => {
        response.data.push(anime);
      });
    }

    return response;
  }

  getAnimes(): Observable<Anime[]> {
    return this.http.get<JikanResponse>(this.API_URL).pipe(
      map((response: JikanResponse) => {
        return response.data.map(this.mapToAnime);
      })
    );
  }

  private mapToAnime(item: JikanAnime): Anime {
    return {
      id: item.mal_id,
      title: item.title || item.title_english || '',
      author: item.studios?.length > 0 ? item.studios[0].name : 'Unknown',
      genre:
        item.genres?.length > 0
          ? item.genres.map((g) => g.name).join(', ')
          : 'Unknown',
      amountEpisodes: item.episodes || 0,
      image: item.images?.jpg?.image_url || '',
    };
  }
}
