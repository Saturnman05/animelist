import { CommonModule } from '@angular/common';
import {
  AfterViewInit,
  Component,
  ElementRef,
  Input,
  OnDestroy,
  OnInit,
  ViewChild,
} from '@angular/core';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { AnimeCardComponent } from '../anime-card/anime-card.component';
import { Anime } from '../../models/anime.model';
import { Subscription } from 'rxjs';
import { JikanAnimeService } from '../../services/jikan-anime/jikan-anime.service';

@Component({
  selector: 'app-anime-grid',
  imports: [AnimeCardComponent, CommonModule, MatProgressSpinnerModule],
  templateUrl: './anime-grid.component.html',
  styleUrl: './anime-grid.component.css',
})
export class AnimeGridComponent implements OnInit, AfterViewInit, OnDestroy {
  animes: Anime[] = [];
  currentPage = 1;
  hasMoreAnimes = true;
  loading = false;

  private observer: IntersectionObserver | null = null;
  private subscription: Subscription | null = null;

  @ViewChild('scrollTrigger') scrollTrigger?: ElementRef;

  constructor(private animeService: JikanAnimeService) {}

  ngOnInit(): void {
    this.loadAnimes();
  }

  ngAfterViewInit(): void {
    this.setupIntersectionObserver();
  }

  ngOnDestroy(): void {
    if (this.observer) {
      this.observer.disconnect();
    }

    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  private setupIntersectionObserver() {
    if (!this.scrollTrigger) return;

    console.log('holaaa');

    const options = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1,
    };

    this.observer = new IntersectionObserver((entries) => {
      const [entry] = entries;
      if (entry.isIntersecting && !this.loading && this.hasMoreAnimes) {
        this.loadMoreAnimes();
      }
    }, options);

    this.observer.observe(this.scrollTrigger.nativeElement);
  }

  private loadAnimes() {
    this.loading = true;

    this.subscription = this.animeService
      .getAnimes(this.currentPage)
      .subscribe({
        next: (result) => {
          this.animes = result.animes;
          this.hasMoreAnimes = result.hasNextPage;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error al cargar animes:', error);
          this.loading = false;
        },
      });
  }

  private loadMoreAnimes() {
    if (this.loading || !this.hasMoreAnimes) return;

    this.loading = true;
    this.currentPage++;

    this.subscription = this.animeService
      .getAnimes(this.currentPage)
      .subscribe({
        next: (result) => {
          this.animes = [...this.animes, ...result.animes];
          this.hasMoreAnimes = result.hasNextPage;
          this.loading = false;
        },
        error: (error) => {
          console.error('Error al cargar más animes:', error);
          this.loading = false;
          this.currentPage--;
        },
      });
  }
}
