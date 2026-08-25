class WebGroundedSourceCitedSearchAnswerSynthesizerClient:
    def synthesize_grounded_web_answer(self, search_prompt='Latest commercial fusion net energy gain benchmarks announced in 2026', recency_filter='PAST_24_HOURS'):
        return {
            'search_session_id': 'ppx_src_5519',
            'prompt': search_prompt,
            'recency_window': recency_filter,
            'live_web_domains_crawled_count': 18,
            'inline_academic_source_citations': [
                {'citation_index': 1, 'domain': 'nature.com', 'title': 'High-temperature superconducting magnet plasma confinement breakthroughs'},
                {'citation_index': 2, 'domain': 'iter.org', 'title': 'Magnet pulse duration record validation'}
            ],
            'groundedness_faithfulness_score_pct': 99.2,
            'follow_up_discovery_questions': ['What are the neutron wall load challenges?', 'Which private fusion startups achieved Q>1?']
        }
