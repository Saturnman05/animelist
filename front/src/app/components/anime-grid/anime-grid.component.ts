import { CommonModule } from '@angular/common';
import { Component, inject, OnInit } from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { AnimeCardComponent } from '../anime-card/anime-card.component';
import { Anime } from '../../models/anime.model';
import { JikanAnimeService } from '../../services/jikan-anime/jikan-anime.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-anime-grid',
  imports: [AnimeCardComponent, CommonModule, MatProgressSpinnerModule],
  templateUrl: './anime-grid.component.html',
  styleUrl: './anime-grid.component.css',
})
export class AnimeGridComponent implements OnInit {
  animes: Anime[] = [];
  currentPage = 1;
  hasMoreAnimes = true;
  loading = false;

  private animeService = inject(JikanAnimeService);
  private router = inject(Router);

  ngOnInit(): void {
    this.loadAnimes();
  }

  onPageScroll(event: any): void {
    if (this.loading || !this.hasMoreAnimes) return;

    const scrollTop = event.target.scrollTop;
    const scrollHeight = event.target.scrollHeight;
    const offsetHeight = event.target.offsetHeight;

    if (scrollHeight - (scrollTop + offsetHeight) < 50 && !this.loading) {
      this.currentPage++;
      this.loadAnimes();
    }
  }

  loadAnimes(): void {
    this.loading = true;

    this.animeService.getAnimes(this.currentPage).subscribe({
      next: (data: { animes: Anime[]; hasNextPage: boolean }) => {
        this.animes = [...this.animes, ...data.animes];
        this.loading = false;
        this.hasMoreAnimes = data.hasNextPage;
      },
      error: (error) => {
        console.error('Error:', error);
        this.loading = false;
      },
    });
  }

  detail(animeId: number): void {
    this.router.navigate([`/detail-anime/${animeId}`]);
  }
}
