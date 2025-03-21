import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { environment } from '../../../environments/environment';
import { map, Observable } from 'rxjs';
import { Anime, JikanAnime, JikanResponse } from '../../models/anime.model';

@Injectable({
  providedIn: 'root',
})
export class JikanAnimeService {
  private readonly API_URL = `${environment.jikanApiUrl}/anime`;

  constructor(private http: HttpClient) {}

  getAnimes(
    page: number = 1,
    limit: number = 25
  ): Observable<{ animes: Anime[]; hasNextPage: boolean }> {
    return this.http
      .get<JikanResponse>(`${this.API_URL}?page=${page}&limit=${limit}`)
      .pipe(
        map((response: JikanResponse) => {
          return {
            animes: response.data.map(this.mapToAnime),
            hasNextPage: response.pagination.has_next_page,
          };
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
