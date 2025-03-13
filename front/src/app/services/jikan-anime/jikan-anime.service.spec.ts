import { TestBed } from '@angular/core/testing';

import { JikanAnimeService } from './jikan-anime.service';

describe('JikanAnimeService', () => {
  let service: JikanAnimeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(JikanAnimeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
